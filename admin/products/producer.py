# amqps://gmwvpgfv:K1fLeJwX94kUFQk2FSy_AsCfyklJlmMa@puffin.rmq2.cloudamqp.com/gmwvpgfv
import pika
import json
from pika import connection
from pika import channel

params = pika.URLParameters(
    'amqps://gmwvpgfv:K1fLeJwX94kUFQk2FSy_AsCfyklJlmMa@puffin.rmq2.cloudamqp.com/gmwvpgfv')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(body), properties=properties)
