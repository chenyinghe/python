#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in xrange(100):
	channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World! ' + str(i)  )
	print " [x] Sent 'Hello World!'" + str(i)
connection.close()
