from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def updated_Col_ToDate(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = in0.withColumn(
        "ToDate",
        when(col("Season1Date").isNotNull(), to_date(substring(col("Season1Date"), 15, 100), "MM/dd/yyyy"))\
          .otherwise(lit("2014-12-31"))
    )

    return out0
