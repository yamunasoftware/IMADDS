### INIT SCRIPT ###

import pymongo
from backend.environment import fetch
from confluent_kafka.admin import AdminClient, NewTopic

admin_client = AdminClient({'bootstrap.servers': 'kafka:9092'})
admin_client.create_topics([NewTopic(fetch("kafka_topic"), 8, 1)])

client = pymongo.MongoClient(fetch("db_url"))
db = client[fetch("db_name")]
db.create_collection(fetch("db_collection"))