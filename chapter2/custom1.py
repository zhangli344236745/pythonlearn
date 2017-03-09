# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/9
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello2')    #声明，队列名称，和producer创建的重复没有关系

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,         #获取body后执行回调函数
                      queue='hello2',
                      no_ack=True)                #自动应答开启，会给MQ服务器发送一个ack：‘已经收到了’。

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()