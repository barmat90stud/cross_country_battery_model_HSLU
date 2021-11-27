from kafka import KafkaConsumer

# this is using the kafka-python package now,
# but we might replace it with the faust package later
# (we just need to keep the method name get_next_stream_message)

consumer = KafkaConsumer(
    'test',
    # auto_offset_reset='earliest',
    bootstrap_servers=['86.119.35.243:9092']
)


def get_next_stream_message():
    for msg in consumer:
        print(msg)
        yield msg
