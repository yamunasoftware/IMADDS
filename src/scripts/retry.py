### RETRY SCRIPT ###

from backend.environment import fetch
from backend.background import start_spark

spark = start_spark("RetrySession")
failures_df = spark.read \
  .format("mongodb") \
  .option("database", fetch("db_name")) \
  .option("collection", fetch("db_collection")) \
  .load()