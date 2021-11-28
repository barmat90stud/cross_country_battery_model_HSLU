import logging


# heart-beats per minute

MIN_VALUE = 40.0
MAX_VALUE = 200.0

ENERGY_NEEDED_THRESHOLD = 140.0
NEARLY_DYING_THRESHOLD = 185.0

PLOT_TITLE = "Cross-Country Battery Model"


# kafka

KAFKA_BOOTSTRAP_SERVERS = ["10.11.22.33:9092"]
KAFKA_TOPIC_NAME = "all_trainings"
KAFKA_PLOT_FIELD = "BPM"

KAFKA_LOGGING_LEVEL = logging.INFO
