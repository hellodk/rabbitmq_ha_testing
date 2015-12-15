#!/usr/bin/env python
import pika

counter = 0
parameters = pika.URLParameters('amqp://konfilarity:konfilarity@10.60.8.23:5672/%2F')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare('testing')
print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='testing',
                      no_ack=True)

channel.start_consuming()