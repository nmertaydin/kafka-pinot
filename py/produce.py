from kafka import KafkaProducer
from confluent_kafka.admin import AdminClient, NewTopic
import simplejson as json
import random

try:
    print('Hello. I am about to publish messages to Kafka...')
    try:
        admin_client = AdminClient({
            "bootstrap.servers": "kafka:9092"
        })
        topic_list = []
        topic_list.append(NewTopic("poc.topic", 1, 1))
        admin_client.create_topics(topic_list)
    except Exception as ex:
        print(ex)
        pass
    producer = KafkaProducer(value_serializer=lambda v:json.dumps(v).encode('utf-8'),bootstrap_servers='kafka:9092', linger_ms=10)
    people = [
        {"name": "Jane", "surname": "Doe", "bankAccountId": "ABC110"},
        {"name": "Joe", "surname": "Doe", "bankAccountId": "DEF220"},
        {"name": "Bonnie", "surname": "Brown", "bankAccountId": "GHI330"},
        {"name": "Clyde", "surname": "Crimson", "bankAccountId": "JKL440"}
    ]
    id_counter = 1
    while True:
        try:
            person = random.choice(people)
            person["incomingAmount"] = round(random.uniform(10,50), 2)
            person["incomingId"] = id_counter
            producer.send('poc.topic', person)
            producer.flush()
            # print('Sent message with incomingId: {}', id_counter)
            id_counter = id_counter + 1
        except Exception as exc:
            print(exc)
except Exception as e:
    print(e)
    pass