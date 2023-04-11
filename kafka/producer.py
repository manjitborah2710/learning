from kafka import KafkaProducer
import json
import sys
import data

def json_serializer(value):
    return json.dumps(value)

producer = KafkaProducer(bootstrap_servers = ['localhost:9092'])

count = 5
try:
    count = int(sys.argv[1])
except:
    pass

while(count > 0):
    user = data.get_user()
    print(user)
    count = count - 1