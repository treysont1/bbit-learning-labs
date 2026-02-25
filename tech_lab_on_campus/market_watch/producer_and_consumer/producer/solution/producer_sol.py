from producer_interface import mqProducerInterface
import pika
import os

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str):
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()
        

    def setupRMQConnection(self):
        conParams = pika.URLParameters('amqp://rabbitmq?connection_attempts=5&retry_delay=5')
        connection = pika.BlockingConnection(parameters=conParams)

        self.channel = connection.channel()
        

    def publishOrder(self, message):
        self.channel.basic_publish(self.exchange_name, self.routing_key, message)

    
    
    
