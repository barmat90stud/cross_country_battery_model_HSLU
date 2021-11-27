import json

from kafka import KafkaConsumer

# this is using the kafka-python package now,
# but we might replace it with the faust package later
# (we just need to keep the method name get_next_stream_message)

consumer = KafkaConsumer(
    'test',
    # auto_offset_reset='earliest',
    bootstrap_servers=['86.119.35.243:9092']
)

# we use this to return this value
# if kafka has currently not a new value at the moment
# (last_value stores the last kafka value)
last_value = 0


def get_next_stream_message():
    global last_value

    for msg_list in consumer:
        msg = json.loads(msg_list.value)
        bpm = float(msg["bpm"])

        if bpm:
            last_value = bpm
            yield bpm
        else:
            yield last_value
