import json

from kafka import KafkaConsumer


consumer = KafkaConsumer(
    'test',
    auto_offset_reset='earliest',
    bootstrap_servers=['86.119.35.243:9092'],
)


def get_next_stream_message():
    for msg_list in consumer:
        msg = json.loads(msg_list.value)

        if bpm := msg["bpm"]:
            yield float(bpm)
