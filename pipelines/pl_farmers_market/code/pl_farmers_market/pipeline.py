from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *
from prophecy.utils import *
from pl_farmers_market.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_farmers_markets = ds_farmers_markets(spark)
    df_filter_by_zip_length = filter_by_zip_length(spark, df_ds_farmers_markets)
    df_reformatted_market_data = reformatted_market_data(spark, df_filter_by_zip_length)
    df_date_transformation = date_transformation(spark, df_reformatted_market_data)
    df_ds_zipcode_agi = ds_zipcode_agi(spark)
    df_by_zipcode = by_zipcode(spark, df_date_transformation, df_ds_zipcode_agi)
    df_cnt_by_production = cnt_by_production(spark, df_by_zipcode)
    ds_farmers_markets_analysis_min(spark, df_cnt_by_production)

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
