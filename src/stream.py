from pyspark.sql import SparkSession

def create_spark_sessions():
  postgres_spark = SparkSession.builder \
    .appName("mongo") \
    .config("spark.master", "spark://spark-master:7077") \
    .config("spark.jars", "/main/lib/spark-mongodb.jar") \
    .getOrCreate()

  snowflake_spark = SparkSession.builder \
    .appName("snowflake") \
    .config("spark.master", "spark://spark-master:7077") \
    .config("spark.jars", "/main/lib/snowflake-jdbc.jar,/main/src/spark-snowflake.jar") \
    .getOrCreate()
  
  kafka_spark = SparkSession.builder \
    .appName("KafkaStreamReader") \
    .config("spark.master", "spark://spark-master:7077") \
    .config("spark.jars", "/main/lib/spark-kafka.jar") \
    .getOrCreate()
  return postgres_spark, snowflake_spark, kafka_spark

def read_stream(spark, topic):
  kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", topic) \
    .option("startingOffsets", "latest") \
    .load()