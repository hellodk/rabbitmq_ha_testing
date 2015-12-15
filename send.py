#!/usr/bin/env python
import pika

try:
    parameters = pika.URLParameters('amqp://konfilarity:konfilarity@10.60.8.23:5672/%2F')
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue="dk")
    #channel.basic_publish('','hello','message body value',pika.BasicProperties(content_type='text/plain',delivery_mode=1))
    connection.close()
    print 'Executed'
except Exception as ex:
    print 'caught ',ex

