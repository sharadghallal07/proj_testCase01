from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def convert_season1date_to_date(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from pyspark.sql.functions import col, substring, to_date
    out0 = in0.withColumn("ToDate", to_date(substring(col("Season1Date"), 1, 10), "MM/dd/yyyy"))

    return out0
