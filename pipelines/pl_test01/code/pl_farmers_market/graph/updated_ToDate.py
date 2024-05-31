from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def updated_ToDate(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from pyspark.sql.functions import col, when, lit
    from pyspark.sql.types import DateType
    from datetime import datetime
    out0 = in0.withColumn(
        "ToDate",
        when(col("ToDate").contains("January"), lit("2014-01-31"))\
          .when(col("ToDate").contains("February"), lit("2014-02-28"))\
          .when(col("ToDate").contains("March"), lit("2014-03-31"))\
          .when(col("ToDate").contains("April"), lit("2014-04-30"))\
          .when(col("ToDate").contains("May"), lit("2014-05-31"))\
          .when(col("ToDate").contains("June"), lit("2014-06-30"))\
          .when(col("ToDate").contains("July"), lit("2014-07-31"))\
          .when(col("ToDate").contains("August"), lit("2014-08-31"))\
          .when(col("ToDate").contains("September"), lit("2014-09-30"))\
          .when(col("ToDate").contains("October"), lit("2014-10-31"))\
          .when(col("ToDate").contains("November"), lit("2014-11-30"))\
          .when(col("ToDate").contains("December"), lit("2014-12-31"))\
          .otherwise(col("ToDate").cast(DateType()))
    )

    return out0
