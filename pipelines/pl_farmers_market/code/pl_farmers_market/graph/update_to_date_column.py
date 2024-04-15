from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def update_to_date_column(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from pyspark.sql.functions import col, when, lit
    out0 = in0.withColumn(
        "ToDate",
        when(
            (col("Season1Date").contains("June to September")) | (col("Season1Date").contains("July to November")),
            lit("2014-07-01")
          )\
          .otherwise(col("ToDate"))
    )

    return out0
