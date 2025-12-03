from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "machine_id": "excavator_1",
        "temperature": random.randint(40, 120),
        "vibration": random.random(),
        "status": "OK"
    }
    producer.send("iotTopic", data)
    print("Sent:", data)
    time.sleep(2)
