# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/9
import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue1', durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello World3!'

channel.basic_publish(exchange='',
    routing_key='task_queue1',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2, # 消息持久化
    ))

print ' [x] Sent %r' % (message,)

channel.close()