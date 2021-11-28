import json

from kafka import KafkaConsumer

import constants


consumer = KafkaConsumer(
    constants.KAFKA_TOPIC_NAME,
    auto_offset_reset='earliest',
    bootstrap_servers=constants.KAFKA_BOOTSTRAP_SERVERS,
)


def get_next_stream_message():
    for msg_list in consumer:
        msg = json.loads(msg_list.value)

        if bpm := msg["bpm"]:
            yield float(bpm)
