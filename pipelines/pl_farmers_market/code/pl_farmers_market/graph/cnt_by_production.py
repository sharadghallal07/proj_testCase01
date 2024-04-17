from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def cnt_by_production(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("County"), col("Location"))

    return df1.agg(
        count(col("Credit")).alias("Cnt_Credit"), 
        count(col("WIC")).alias("Cnt_WIC"), 
        count(col("WICcash")).alias("Cnt_WICcash"), 
        count(col("SFMNP")).alias("Cnt_SFMNP"), 
        count(col("SNAP")).alias("Cnt_SNAP"), 
        count(col("Organic")).alias("Cnt_Organic"), 
        count(col("Bakedgoods")).alias("Cnt_Bakedgoods"), 
        count(col("Cheese")).alias("Cnt_Cheese"), 
        count(col("Crafts")).alias("Cnt_Crafts"), 
        count(col("Flowers")).alias("Cnt_Flowers"), 
        count(col("Eggs")).alias("Cnt_Eggs"), 
        count(col("Seafood")).alias("Cnt_Seafood"), 
        count(col("Herbs")).alias("Cnt_Herbs"), 
        count(col("Vegetables")).alias("Cnt_Vegetables")
    )
