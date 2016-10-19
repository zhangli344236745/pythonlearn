__author__ = '0138695'
from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer
from kafka.producer import SimpleProducer, KeyedProducer

kafkaclient = KafkaClient()

# To send messages synchronously
producer = SimpleProducer(kafkaclient)
producer.send_messages("test","ewrwer")
producer.send_messages("test", "is variadic")
