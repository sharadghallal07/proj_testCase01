from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def update_to_date(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from pyspark.sql.functions import col, when, lit
    out0 = in0.withColumn(
        "ToDate",
        when(col("Season1Date").like("%January%"), lit("2014-01-01"))\
          .when(col("Season1Date").like("%February%"), lit("2014-02-01"))\
          .when(col("Season1Date").like("%March%"), lit("2014-03-01"))\
          .when(col("Season1Date").like("%April%"), lit("2014-04-01"))\
          .when(col("Season1Date").like("%May%"), lit("2014-05-01"))\
          .when(col("Season1Date").like("%June%"), lit("2014-06-01"))\
          .when(col("Season1Date").like("%July%"), lit("2014-07-01"))\
          .when(col("Season1Date").like("%August%"), lit("2014-08-01"))\
          .when(col("Season1Date").like("%September%"), lit("2014-09-01"))\
          .when(col("Season1Date").like("%October%"), lit("2014-10-01"))\
          .when(col("Season1Date").like("%November%"), lit("2014-11-01"))\
          .when(col("Season1Date").like("%December%"), lit("2014-12-01"))\
          .otherwise(col("ToDate"))
    )

    return out0
