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
    df_updated_Col_FromDate = updated_Col_FromDate(spark, df_reformatted_columns)
    df_updated_Col_ToDate = updated_Col_ToDate(spark, df_updated_Col_FromDate)
    df_updated_FromDate = updated_FromDate(spark, df_updated_Col_ToDate)
    df_inserted_Col_ToDate = inserted_Col_ToDate(spark, df_updated_FromDate)
    df_updated_ToDate = updated_ToDate(spark, df_inserted_Col_ToDate)
    df_create_Col_Source = create_Col_Source(spark, df_updated_ToDate)
    df_fillNa = fillNa(spark, df_create_Col_Source)
    df_ds_zipcode_agi = ds_zipcode_agi(spark)
    df_join_zipcode = join_zipcode(spark, df_fillNa, df_ds_zipcode_agi)
    df_count_cheese_by_county = count_cheese_by_county(spark, df_join_zipcode)
    ds_farmers_markets_analysis(spark, df_count_cheese_by_county)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pl_farmers_market")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_test01")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pl_test01", config = Config)(pipeline)

if __name__ == "__main__":
    main()
