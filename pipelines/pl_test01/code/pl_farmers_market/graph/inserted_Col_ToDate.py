from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def inserted_Col_ToDate(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = in0.withColumn(
        "ToDate",
        when(
            col("Season1Date").like("%to%"),
            when(col("ToDate").isNull(), regexp_extract(col("Season1Date"), r"\b(\w+)\b$", 1)).otherwise(col("ToDate"))
          )\
          .otherwise(col("ToDate"))
    )

    return out0
