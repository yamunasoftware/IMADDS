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

# Fetch JARs Config from Environment Info:
def fetch_jars_config(os):
  config = ""
  count = 0

  for key in _info:
    if '_jar' in key:
      if count >0:
        config += "," + _info[key]
      
      else:
        config += _info[key]
    count += 1
  
  os.environ['CLASSPATH'] = config.replace(',', ':')
  return config

# Gets Credentials:
def get_creds():
  username, password = '', ''
  with open('.auth', 'r') as file:
    contents = file.read()
    lines = contents.split('\n')

    for line in lines:
      if 'USERNAME' in line:
        username = line.replace('USERNAME=', '')
      
      if 'PASSWORD' in line:
        password = line.replace('PASSWORD=', '')
  return username, password