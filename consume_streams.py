import json
import logging
import sys

from kafka import KafkaConsumer

import constants


logging.basicConfig(stream=sys.stdout, level=constants.KAFKA_LOGGING_LEVEL)

consumer = KafkaConsumer(
    constants.KAFKA_TOPIC_NAME,
    auto_offset_reset='earliest',
    bootstrap_servers=constants.KAFKA_BOOTSTRAP_SERVERS,
)
logging.info("created kafka consumer")


def get_next_stream_message():
    for msg_list in consumer:
        msg = json.loads(msg_list.value)
        logging.info(f"kafka message = {str(msg)}")

        if msg_field := msg[constants.KAFKA_PLOT_FIELD]:
            yield float(msg_field)
