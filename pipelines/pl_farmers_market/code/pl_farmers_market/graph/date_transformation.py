from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def date_transformation(spark: SparkSession, in0: DataFrame) -> DataFrame:
    from pyspark.sql.functions import col, lit, when, substring, to_date, regexp_extract, concat_ws, coalesce
    from pyspark.sql.types import DateType
    # Fill null values with empty strings
    #in0 = in0.fillna("")
    # Define the transformations using withColumn
    out0 = in0\
               .withColumn(
                 "FromDate",
                 when(col("Season1Date").isNotNull(), to_date(substring(col("Season1Date"), 1, 10), "MM/dd/yyyy"))\
                   .otherwise(lit("2014-01-01"))
               )\
               .withColumn(
                 "ToDate",
                 when(col("Season1Date").isNotNull(), to_date(substring(col("Season1Date"), 15, 100), "MM/dd/yyyy"))\
                   .otherwise(lit("2014-12-31"))
               )\
               .withColumn(
                 "FromDate",
                 when(col("Season1Date").rlike(r"\bJanuary\b"), lit("2014-01-01"))\
                   .when(col("Season1Date").rlike(r"\bFebruary\b"), lit("2014-02-01"))\
                   .when(col("Season1Date").rlike(r"\bMarch\b"), lit("2014-03-01"))\
                   .when(col("Season1Date").rlike(r"\bApril\b"), lit("2014-04-01"))\
                   .when(col("Season1Date").rlike(r"\bMay\b"), lit("2014-05-01"))\
                   .when(col("Season1Date").rlike(r"\bJune\b"), lit("2014-06-01"))\
                   .when(col("Season1Date").rlike(r"\bJuly\b"), lit("2014-07-01"))\
                   .when(col("Season1Date").rlike(r"\bAugust\b"), lit("2014-08-01"))\
                   .when(col("Season1Date").rlike(r"\bSeptember\b"), lit("2014-09-01"))\
                   .when(col("Season1Date").rlike(r"\bOctober\b"), lit("2014-10-01"))\
                   .when(col("Season1Date").rlike(r"\bNovember\b"), lit("2014-11-01"))\
                   .when(col("Season1Date").rlike(r"\bDecember\b"), lit("2014-12-01"))\
                   .otherwise(col("FromDate"))
               )\
               .withColumn(
                 "ToDate",
                 when(
                     col("Season1Date").like("%to%"),
                     when(col("ToDate").isNull(), regexp_extract(col("Season1Date"), r"\b(\w+)\b$", 1))\
                       .otherwise(col("ToDate"))
                   )\
                   .otherwise(col("ToDate"))
               )\
               .withColumn(
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
               )\
               .withColumn(
                 "Source",
                 concat_ws(
                   '',
                   coalesce(col("Website"), lit('')),
                   coalesce(col("Facebook"), lit('')),
                   coalesce(col("Twitter"), lit('')),
                   coalesce(col("Youtube"), lit('')),
                   coalesce(col("OtherMedia"), lit(''))
                 )
               )\
               .fillna("")

    return out0
