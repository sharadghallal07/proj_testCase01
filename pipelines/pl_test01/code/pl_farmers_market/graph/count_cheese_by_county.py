from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def count_cheese_by_county(spark: SparkSession, in0: DataFrame) -> DataFrame:
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
        count(col("Vegetables")).alias("Cnt_Vegetables"), 
        count(col("Honey")).alias("Cnt_Honey"), 
        count(col("Jams")).alias("Cnt_Jams"), 
        count(col("Maple")).alias("Cnt_Maple"), 
        count(col("Meat")).alias("Cnt_Meat"), 
        count(col("Nursery")).alias("Cnt_Nursery"), 
        count(col("Nuts")).alias("Cnt_Nuts"), 
        count(col("Plants")).alias("Cnt_Plants"), 
        count(col("Poultry")).alias("Cnt_Poultry"), 
        count(col("Prepared")).alias("Cnt_Prepared"), 
        count(col("Soap")).alias("Cnt_Soap"), 
        count(col("Trees")).alias("Cnt_Trees"), 
        count(col("Wine")).alias("Cnt_Wine"), 
        count(col("Coffee")).alias("Cnt_Coffee"), 
        count(col("Beans")).alias("Cnt_Beans"), 
        count(col("Fruits")).alias("Cnt_Fruits"), 
        count(col("Grains")).alias("Cnt_Grains"), 
        count(col("Juices")).alias("Cnt_Juices"), 
        count(col("Mushrooms")).alias("Cnt_Mushrooms"), 
        count(col("PetFood")).alias("Cnt_PetFood"), 
        count(col("Tofu")).alias("Cnt_Tofu"), 
        count(col("WildHarvested")).alias("Cnt_WildHarvested")
    )
