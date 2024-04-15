from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *
from prophecy.utils import *
from pl_farmers_market.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_farmers_markets = ds_farmers_markets(spark)
    df_zip_clean = zip_clean(spark, df_ds_farmers_markets)
    df_reformatted_columns = reformatted_columns(spark, df_zip_clean)
    df_convert_season1_date = convert_season1_date(spark, df_reformatted_columns)
    df_updated_Col_FromDate = updated_Col_FromDate(spark, df_reformatted_columns)
    df_updated_Col_ToDate = updated_Col_ToDate(spark, df_updated_Col_FromDate)
    df_add_columns = add_columns(spark, df_zip_clean)
    df_convert_season1date_to_date = convert_season1date_to_date(spark, df_zip_clean)
    df_updated_FromDate = updated_FromDate(spark, df_updated_Col_ToDate)
    df_inserted_Col_ToDate = inserted_Col_ToDate(spark, df_updated_FromDate)
    df_convert_season1date_to_date_1 = convert_season1date_to_date_1(spark, df_reformatted_columns)
    df_update_to_date = update_to_date(spark, df_convert_season1date_to_date_1)
    df_replace_season1_date_with_to_date = replace_season1_date_with_to_date(spark, df_reformatted_columns)
    df_update_to_date_column = update_to_date_column(spark, df_replace_season1_date_with_to_date)
    df_updated_ToDate = updated_ToDate(spark, df_inserted_Col_ToDate)
    df_create_Col_Source = create_Col_Source(spark, df_updated_ToDate)
    df_ds_zipcode_agi = ds_zipcode_agi(spark)
    df_by_zipcode = by_zipcode(spark, df_create_Col_Source, df_ds_zipcode_agi)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_farmers_market")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_farmers_market")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_farmers_market", config = Config)(pipeline)

if __name__ == "__main__":
    main()
