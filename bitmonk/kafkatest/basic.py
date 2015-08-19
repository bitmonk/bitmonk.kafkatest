import logging,time
from pykafka import KafkaClient

logger = logging.getLogger('pykafka.cluster')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

client = KafkaClient(hosts='10.100.6.241:9092,10.100.6.242:9092,10.100.6.243:9092')
topic = client.topics['bitmonk2']
p = topic.get_producer()

for i in range(86400):
  p.produce(["message %s" % str(i)])
  time.sleep(0.01)

