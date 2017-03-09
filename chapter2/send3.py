# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/9
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logzl',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: zhangli Hello World!"
channel.basic_publish(exchange='logzl',
                      routing_key='',
                      body=message)
print " [x] Sent %r" % (message,)
connection.close()