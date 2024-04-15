from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def add_columns(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from pyspark.sql.functions import col, when, lit, to_date
    out0 = in0.withColumn(
        "ToDate",
        when(col("Season1Date").isNull(), lit("01-01-2014")).otherwise(to_date(col("Season1Date"), "MM-dd-yyyy"))
    )

    return out0
