# Private Environment Info:
_info = {
  "db_url": "mongodb://admin:password@imaddsdb:27017",
  "db_name": "events",
  "db_collection": "failures",
  "kafka_url": "kafka:9092",
  "kafka_topic": "IMADDS",
  "kafka_jar": "/main/lib/spark-kafka.jar",
  "snowflake_jars": "/main/lib/snowflake-jdbc.jar,/main/src/spark-snowflake.jar",
  "mongo_jar": "/main/lib/spark-mongodb.jar",
  "models_path": "/main/models"
}

# Fetch Data from Environment Info:
def fetch(key):
  return _info[key]

# Fetch All Data from Environment Info:
def fetch_all():
  return _info

# Gets SnowFlake Auth Credentials:
def get_snowflake_auth():
  options = {}
  with open('/main/src/.auth', 'r') as file:
    contents = file.read()
    lines = contents.split('\n')

    for line in lines:
      if 'URL' in line:
        options["sfURL"] = line.replace('URL=', '')

      if 'USERNAME' in line:
        options["sfUser"] = line.replace('USERNAME=', '')
      
      if 'PASSWORD' in line:
        options["sfPassword"] = line.replace('PASSWORD=', '')

      if 'DATABASE' in line:
        options["sfDatabase"] = line.replace('DATABASE=', '')

      if 'SCHEMA' in line:
        options["sfSchema"] = line.replace('SCHEMA=', '')

      if 'WAREHOUSE' in line:
        options["sfWarehouse"] = line.replace('WAREHOUSE=', '')
  return options