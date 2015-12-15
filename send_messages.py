#!/usr/bin/env python
import pika
import time

counter = 0
parameters = pika.URLParameters('amqp://konfilarity:konfilarity@10.60.8.23:5672/%2F')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='testing')
while(1):
    channel.basic_publish('','testing','dk')
    counter = counter+1
    print counter,'data sent'
connection.close()

