# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/9

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()    #创建通道

channel.queue_declare(queue='hello2')    #队列名称

channel.basic_publish(exchange='',
                      routing_key='hello2',  #路由名称
                      body='Hello World2!')  #发送内容
print(" [x] Sent 'Hello World!'")
connection.close()