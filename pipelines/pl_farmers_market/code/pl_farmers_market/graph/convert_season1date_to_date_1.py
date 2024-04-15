from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def convert_season1date_to_date_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = in0.withColumn(
        "FromDate",
        when(col("Season1Date").isNotNull(), to_date(col("Season1Date"), "MM/dd/yyyy")).otherwise(col("FromDate"))
    )
    out0 = out0.withColumn(
        "ToDate",
        when(col("Season1Date").isNotNull(), to_date(col("Season1Date"), "MM/dd/yyyy")).otherwise(col("ToDate"))
    )

    return out0
