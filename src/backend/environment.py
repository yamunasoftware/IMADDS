# Private Environment Info:
_info = {
  "db_url": "mongodb://admin:password@imaddsdb:27017/events",
  "kafka_url": "kafka:9092",
  "kafka_topic": "IMADDS",
  "kafka_jar": "/main/lib/spark-kafka.jar",
  "snowflake_jars": "/main/lib/snowflake-jdbc.jar,/main/src/spark-snowflake.jar",
  "mongo_jar": "/main/lib/spark-mongodb.jar"
}

# Fetch Data from Environment Info:
def fetch(key):
  return _info[key]

# Fetch All Data from Environment Info:
def fetch_all():
  return _info