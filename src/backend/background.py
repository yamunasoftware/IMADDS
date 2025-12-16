import os
from backend.environment import fetch, fetch_all
from pyspark.sql import SparkSession

# Gets Auth Credentials:
def get_auth_creds():
  url, username, password = '', '', ''
  with open('/main/src/.auth', 'r') as file:
    contents = file.read()
    lines = contents.split('\n')

    for line in lines:
      if 'URL' in line:
        url = line.replace('URL=', '')

      if 'USERNAME' in line:
        username = line.replace('USERNAME=', '')
      
      if 'PASSWORD' in line:
        password = line.replace('PASSWORD=', '')
  return url, username, password

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

# Writes Data to Snowflake:
def write_snowflake(spark, data):
  return 0

# Reads Data from MongoDB:
def read_mongo(spark, query):
  return 0

# Writes Message to MongoDB:
def write_mongo(spark, data):
  return 0
