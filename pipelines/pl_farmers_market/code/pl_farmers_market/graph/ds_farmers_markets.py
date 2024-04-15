from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def ds_farmers_markets(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("FMID", LongType(), True), StructField("MarketName", StringType(), True), StructField("Website", StringType(), True), StructField("Facebook", StringType(), True), StructField("Twitter", StringType(), True), StructField("Youtube", StringType(), True), StructField("OtherMedia", StringType(), True), StructField("street", StringType(), True), StructField("city", StringType(), True), StructField("County", StringType(), True), StructField("State", StringType(), True), StructField("zip", IntegerType(), True), StructField("Season1Date", StringType(), True), StructField("Season1Time", StringType(), True), StructField("Season2Date", StringType(), True), StructField("Season2Time", StringType(), True), StructField("Season3Date", StringType(), True), StructField("Season3Time", StringType(), True), StructField("Season4Date", StringType(), True), StructField("Season4Time", StringType(), True), StructField("x", DecimalType(20, 10), True), StructField("y", DecimalType(20, 10), True), StructField("Location", StringType(), True), StructField("Credit", StringType(), True), StructField("WIC", StringType(), True), StructField("WICcash", StringType(), True), StructField("SFMNP", StringType(), True), StructField("SNAP", StringType(), True), StructField("Organic", StringType(), True), StructField("Bakedgoods", StringType(), True), StructField("Cheese", StringType(), True), StructField("Crafts", StringType(), True), StructField("Flowers", StringType(), True), StructField("Eggs", StringType(), True), StructField("Seafood", StringType(), True), StructField("Herbs", StringType(), True), StructField("Vegetables", StringType(), True), StructField("Honey", StringType(), True), StructField("Jams", StringType(), True), StructField("Maple", StringType(), True), StructField("Meat", StringType(), True), StructField("Nursery", StringType(), True), StructField("Nuts", StringType(), True), StructField("Plants", StringType(), True), StructField("Poultry", StringType(), True), StructField("Prepared", StringType(), True), StructField("Soap", StringType(), True), StructField("Trees", StringType(), True), StructField("Wine", StringType(), True), StructField("Coffee", StringType(), True), StructField("Beans", StringType(), True), StructField("Fruits", StringType(), True), StructField("Grains", StringType(), True), StructField("Juices", StringType(), True), StructField("Mushrooms", StringType(), True), StructField("PetFood", StringType(), True), StructField("Tofu", StringType(), True), StructField("WildHarvested", StringType(), True), StructField("updateTime", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/databricks-datasets/data.gov/farmers_markets_geographic_data/data-001/market_data.csv")
