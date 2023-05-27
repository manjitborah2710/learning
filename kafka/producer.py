from kafka import KafkaProducer
import json
import sys
import data
import time

def json_serializer(value):
    return json.dumps(value).encode('utf-8')

def send_to_kafka(producer, message, topic):
    producer.send(topic, message)


producer = KafkaProducer(bootstrap_servers = ['localhost:9092'], value_serializer = json_serializer)

count = 5
try:
    count = int(sys.argv[1])
except:
    pass

while(count > 0):
    user = data.get_user()
    print(user)
    send_to_kafka(producer, user, 'test_topic')
    time.sleep(4)
    count = count - 1