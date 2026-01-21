### RETRY SCRIPT ###

import time
from backend.background import start_spark, write_snowflake, read_mongo

while True:
  spark = start_spark("RetrySession")
  failures_df = read_mongo(spark)

  if not failures_df.isEmpty():
    write_snowflake(failures_df, None)
  spark.stop()
  time.sleep(1800)