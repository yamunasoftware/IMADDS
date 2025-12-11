### RETRY IMPORTS ###

import os
from info import fetch, fetch_jars_config, get_creds
from stream import write_snowflake
from pyspark.sql import SparkSession

### RETRY FUNCTIONS ###

def read_mongo(spark, data):
  return 0

### RETRY RUNNING ###

spark = SparkSession.builder \
  .appName("RetrySnowflake") \
  .config("spark.master", "spark://spark-master:7077") \
  .config("spark.jars", fetch_jars_config(os)) \
  .getOrCreate()