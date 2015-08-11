import logging
from pykafka import KafkaClient

logger = logging.getLogger('pykafka.cluster')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

client = KafkaClient(hosts='10.100.6.241:9092,10.100.6.242:9092,10.100.6.243:9092')

