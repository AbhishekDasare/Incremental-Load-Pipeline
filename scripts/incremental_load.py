from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Incremental Load Pipeline") \
    .getOrCreate()

source_df = spark.read.csv(
    "data/source/customer_data.csv",
    header=True,
    inferSchema=True
)

incremental_df = spark.read.csv(
    "data/incremental/new_customer_data.csv",
    header=True,
    inferSchema=True
)

final_df = source_df.union(incremental_df)

final_df.write.mode("overwrite").csv(
    "data/target",
    header=True
)

final_df.show()

spark.stop()
