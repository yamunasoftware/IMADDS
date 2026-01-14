### STREAM SCRIPT ###

from backend.model import load_models, predict_model
from backend.environment import fetch
from backend.background import start_spark

models = load_models()
spark = start_spark("KafkaStreamReader")
kafka_df = spark.readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", fetch("kafka_url")) \
  .option("subscribe", fetch("kafka_topic")) \
  .option("startingOffsets", "latest") \
  .load()

#converted_df = kafka_df.toPandas()
#prediction = predict_model(models['model.pkl'], converted_df)
query = kafka_df.writeStream \
  .outputMode("append") \
  .format("console") \
  .start()
query.awaitTermination() 