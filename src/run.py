import stream
from confluent_kafka.admin import AdminClient, NewTopic

# Creates Kafka Topic From Config:
topic = 'IMADDS'
admin_client = AdminClient({'bootstrap.servers': 'kafka:9092'})
admin_client.create_topics([NewTopic(topic, 8, 1)])

# Starts IMADDS Streaming:
mongo_spark, snowflake_spark, kafka_spark = stream.create_spark_sessions()
stream.read_stream(kafka_spark, topic)