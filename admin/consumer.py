# amqps://gmwvpgfv:K1fLeJwX94kUFQk2FSy_AsCfyklJlmMa@puffin.rmq2.cloudamqp.com/gmwvpgfv

import pika
import json
import os
import django
from pika import connection
from pika import channel
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()


params = pika.URLParameters(
    'amqps://gmwvpgfv:K1fLeJwX94kUFQk2FSy_AsCfyklJlmMa@puffin.rmq2.cloudamqp.com/gmwvpgfv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):

    from products.models import Product
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes += 1
    product.save()
    print('Product likes increased')


channel.basic_consume(
    queue='admin', on_message_callback=callback, auto_ack=True)
print('started consuming')

channel.start_consuming()
channel.close()
