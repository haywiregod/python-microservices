import pika
import json
from pika import connection
from pika import channel

params = pika.URLParameters(
    'rabbit_MQ_URL_HERE')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin',
                          body=json.dumps(body), properties=properties)
