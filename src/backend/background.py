import os
from backend.environment import fetch, fetch_all, get_snowflake_auth
from pyspark.sql import SparkSession

import datetime
import logging
logging.basicConfig(level=logging.INFO)

# Starts Spark Session:
def start_spark(name):
  return SparkSession.builder \
  .appName(name) \
  .config("spark.master", "spark://spark-master:7077") \
  .config("spark.jars", jars_config()) \
  .config("spark.mongodb.input.uri", fetch("db_url")) \
  .config("spark.mongodb.output.uri", fetch("db_url")) \
  .getOrCreate()

# JARs Config from Environment Info:
def jars_config():
  config = ""
  info = fetch_all()

  count = 0
  for key in info:
    if '_jar' in key:
      if count >0:
        config += "," + info[key]
      
      else:
        config += info[key]
    count += 1
  
  os.environ['CLASSPATH'] = config.replace(',', ':')
  return config

# Writes Message to Snowflake:
def write_snowflake(batch_df, batch_id):
  try:
    batch_df.write \
      .format("net.snowflake.spark.snowflake") \
      .options(**get_snowflake_auth()) \
      .option("dbtable", fetch("snowflake_table")) \
      .mode("append") \
      .save()
    
  except Exception as e:
    logging.error(datetime.now() + " - Failed to Write to SnowFlake, Writing to MongoDB...")
    _write_mongo(batch_df, batch_id)
  
# Writes Message to MongoDB:
def _write_mongo(batch_df, batch_id):
  try:
    batch_df.write \
      .format("mongodb") \
      .option("database", fetch("db_name")) \
      .option("collection", fetch("db_collection")) \
      .mode("append") \
      .save()
    
  except Exception as e:
    logging.error(datetime.now() + " - Failed to Write to MongoDB")

# Reads Messages from MongoDB:
def read_mongo(spark):
  return spark.read \
    .format("mongodb") \
    .option("database", fetch("db_name")) \
    .option("collection", fetch("db_collection")) \
    .load()