### STREAM IMPORTS ###

import os
from info import fetch, fetch_jars_config, get_creds
from pyspark.sql import SparkSession

### STREAM FUNCTIONS ###

def write_snowflake(spark, data):
  return 0
  
def write_mongo(spark, data):
  return 0

### STREAM RUNNING ###

spark = SparkSession.builder \
  .appName("KafkaStreamReader") \
  .config("spark.master", "spark://spark-master:7077") \
  .config("spark.jars", fetch_jars_config(os)) \
  .getOrCreate()

kafka_df = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", fetch("kafka_url")) \
  .option("subscribe", fetch("kafka_topic")) \
  .option("startingOffsets", "latest") \
  .load()