from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_farmers_market.config.ConfigStore import *
from pl_farmers_market.udfs.UDFs import *

def by_zipcode(spark: SparkSession, in0: DataFrame, in1: DataFrame, ) -> DataFrame:
    return in0\
        .alias("in0")\
        .join(in1.alias("in1"), (col("in0.zip") == col("in1.zipcode")), "inner")\
        .select(col("in0.FMID").alias("FMID"), col("in0.MarketName").alias("MarketName"), col("in0.Website").alias("Website"), col("in0.Facebook").alias("Facebook"), col("in0.Twitter").alias("Twitter"), col("in0.Youtube").alias("Youtube"), col("in0.OtherMedia").alias("OtherMedia"), col("in0.Source").alias("Source"), col("in0.street").alias("street"), col("in0.city").alias("city"), col("in0.County").alias("County"), col("in0.State").alias("State"), col("in0.zip").alias("zip"), col("in0.Season1Date").alias("Season1Date"), col("in0.FromDate").alias("FromDate"), col("in0.ToDate").alias("ToDate"), col("in0.Season1Time").alias("Season1Time"), col("in0.Season2Date").alias("Season2Date"), col("in0.Season2Time").alias("Season2Time"), col("in0.Season3Date").alias("Season3Date"), col("in0.Season3Time").alias("Season3Time"), col("in0.Season4Date").alias("Season4Date"), col("in0.Season4Time").alias("Season4Time"), col("in0.x").alias("x"), col("in0.y").alias("y"), col("in0.Location").alias("Location"), col("in0.Credit").alias("Credit"), col("in0.WIC").alias("WIC"), col("in0.WICcash").alias("WICcash"), col("in0.SFMNP").alias("SFMNP"), col("in0.SNAP").alias("SNAP"), col("in0.Organic").alias("Organic"), col("in0.Bakedgoods").alias("Bakedgoods"), col("in0.Cheese").alias("Cheese"), col("in0.Crafts").alias("Crafts"), col("in0.Flowers").alias("Flowers"), col("in0.Eggs").alias("Eggs"), col("in0.Seafood").alias("Seafood"), col("in0.Herbs").alias("Herbs"), col("in0.Vegetables").alias("Vegetables"), col("in0.Honey").alias("Honey"), col("in0.Jams").alias("Jams"), col("in0.Maple").alias("Maple"), col("in0.Meat").alias("Meat"), col("in0.Nursery").alias("Nursery"), col("in0.Nuts").alias("Nuts"), col("in0.Plants").alias("Plants"), col("in0.Poultry").alias("Poultry"), col("in0.Prepared").alias("Prepared"), col("in0.Soap").alias("Soap"), col("in0.Trees").alias("Trees"), col("in0.Wine").alias("Wine"), col("in0.Coffee").alias("Coffee"), col("in0.Beans").alias("Beans"), col("in0.Fruits").alias("Fruits"), col("in0.Grains").alias("Grains"), col("in0.Juices").alias("Juices"), col("in0.Mushrooms").alias("Mushrooms"), col("in0.PetFood").alias("PetFood"), col("in0.Tofu").alias("Tofu"), col("in0.WildHarvested").alias("WildHarvested"), col("in0.updateTime").alias("updateTime"), col("in1.STATEFIPS").alias("STATEFIPS"), col("in1.STATE").alias("STATE"), col("in1.agi_stub").alias("agi_stub"), col("in1.N1").alias("N1"), col("in1.MARS1").alias("MARS1"), col("in1.MARS2").alias("MARS2"), col("in1.MARS4").alias("MARS4"), col("in1.PREP").alias("PREP"), col("in1.N2").alias("N2"), col("in1.NUMDEP").alias("NUMDEP"), col("in1.A00100").alias("A00100"), col("in1.N02650").alias("N02650"), col("in1.A02650").alias("A02650"), col("in1.N00200").alias("N00200"), col("in1.A00200").alias("A00200"), col("in1.N00300").alias("N00300"), col("in1.A00300").alias("A00300"), col("in1.N00600").alias("N00600"), col("in1.A00600").alias("A00600"), col("in1.N00650").alias("N00650"), col("in1.A00650").alias("A00650"), col("in1.N00700").alias("N00700"), col("in1.A00700").alias("A00700"), col("in1.N00900").alias("N00900"), col("in1.A00900").alias("A00900"), col("in1.N01000").alias("N01000"), col("in1.A01000").alias("A01000"), col("in1.N01400").alias("N01400"), col("in1.A01400").alias("A01400"), col("in1.N01700").alias("N01700"), col("in1.A01700").alias("A01700"), col("in1.SCHF").alias("SCHF"), col("in1.N02300").alias("N02300"), col("in1.A02300").alias("A02300"), col("in1.N02500").alias("N02500"), col("in1.A02500").alias("A02500"), col("in1.N26270").alias("N26270"), col("in1.A26270").alias("A26270"), col("in1.N02900").alias("N02900"), col("in1.A02900").alias("A02900"), col("in1.N03220").alias("N03220"), col("in1.A03220").alias("A03220"), col("in1.N03300").alias("N03300"), col("in1.A03300").alias("A03300"), col("in1.N03270").alias("N03270"), col("in1.A03270").alias("A03270"), col("in1.N03150").alias("N03150"), col("in1.A03150").alias("A03150"), col("in1.N03210").alias("N03210"), col("in1.A03210").alias("A03210"), col("in1.N03230").alias("N03230"), col("in1.A03230").alias("A03230"), col("in1.N03240").alias("N03240"), col("in1.A03240").alias("A03240"), col("in1.N04470").alias("N04470"), col("in1.A04470").alias("A04470"), col("in1.A00101").alias("A00101"), col("in1.N18425").alias("N18425"), col("in1.A18425").alias("A18425"), col("in1.N18450").alias("N18450"), col("in1.A18450").alias("A18450"), col("in1.N18500").alias("N18500"), col("in1.A18500").alias("A18500"), col("in1.N18300").alias("N18300"), col("in1.A18300").alias("A18300"), col("in1.N19300").alias("N19300"), col("in1.A19300").alias("A19300"), col("in1.N19700").alias("N19700"), col("in1.A19700").alias("A19700"), col("in1.N04800").alias("N04800"), col("in1.A04800").alias("A04800"), col("in1.N05800").alias("N05800"), col("in1.A05800").alias("A05800"), col("in1.N09600").alias("N09600"), col("in1.A09600").alias("A09600"), col("in1.N07100").alias("N07100"), col("in1.A07100").alias("A07100"), col("in1.N07300").alias("N07300"), col("in1.A07300").alias("A07300"), col("in1.N07180").alias("N07180"), col("in1.A07180").alias("A07180"), col("in1.N07230").alias("N07230"), col("in1.A07230").alias("A07230"), col("in1.N07240").alias("N07240"), col("in1.A07240").alias("A07240"), col("in1.N07220").alias("N07220"), col("in1.A07220").alias("A07220"), col("in1.N07260").alias("N07260"), col("in1.A07260").alias("A07260"), col("in1.N09400").alias("N09400"), col("in1.A09400").alias("A09400"), col("in1.N10600").alias("N10600"), col("in1.A10600").alias("A10600"), col("in1.N59660").alias("N59660"), col("in1.A59660").alias("A59660"), col("in1.N59720").alias("N59720"), col("in1.A59720").alias("A59720"), col("in1.N11070").alias("N11070"), col("in1.A11070").alias("A11070"), col("in1.N10960").alias("N10960"), col("in1.A10960").alias("A10960"), col("in1.N06500").alias("N06500"), col("in1.A06500").alias("A06500"), col("in1.N10300").alias("N10300"), col("in1.A10300").alias("A10300"), col("in1.N85330").alias("N85330"), col("in1.A85330").alias("A85330"), col("in1.N85300").alias("N85300"), col("in1.A85300").alias("A85300"), col("in1.N11901").alias("N11901"), col("in1.A11901").alias("A11901"), col("in1.N11902").alias("N11902"), col("in1.A11902").alias("A11902"))
