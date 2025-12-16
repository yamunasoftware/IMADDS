### STREAM SCRIPT ###

from backend.environment import fetch
from backend.background import start_spark

spark = start_spark("KafkaStreamReader")
kafka_df = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", fetch("kafka_url")) \
  .option("subscribe", fetch("kafka_topic")) \
  .option("startingOffsets", "latest") \
  .load()

query = kafka_df.writeStream \
  .outputMode("append") \
  .format("console") \
  .start()
query.awaitTermination() 