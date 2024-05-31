from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def zip_clean(spark: SparkSession, in0: DataFrame) -> DataFrame:
    out0 = in0.filter(col("zip").isNotNull() & (length(col("zip")) == 5))

    return out0
