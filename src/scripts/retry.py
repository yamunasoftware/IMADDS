### RETRY SCRIPT ###

import time
from backend.environment import fetch, get_snowflake_auth
from backend.background import start_spark

while True:
  spark = start_spark("RetrySession")
  failures_df = spark.read \
    .format("mongodb") \
    .option("database", fetch("db_name")) \
    .option("collection", fetch("db_collection")) \
    .load()

  if not failures_df.isEmpty():
    failures_df.write \
      .format("net.snowflake.spark.snowflake") \
      .options(**get_snowflake_auth()) \
      .option("dbtable", "IMADDS") \
      .mode("append") \
      .save()
  spark.stop()
  time.sleep(1800)