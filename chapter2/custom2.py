# -*- coding: utf-8 -*-
# Created by 0138695 on 2017/3/9
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# 参数durable设置为True表明队列是持久化
# 如果只是在这个文件声明队列是持久化的，但是在另一个创建队列的地方没有声明持久化，就会报错
# 因为在创建队列的时候，创建的队列的名字是一样的，但是属性不一样，所以会报错
# 这样做只是实现了队列的持久化还需要将消息设置为持久化
channel.queue_declare(queue='task_queue1', durable=True)

def callback(ch, method, properties, body):
    print ' [x] Received %r' % (body,)
    time.sleep(body.count('.'))
    print ' [x] Done'
    # 为什么加上这句话？
    # 在没有加上这句话之前，发布者发送了四个任务到队列中，虽然都被消费者取走，但是图形化界面
    # 上显示Unacked还是4，表示四个消息没有得到消费者的确认，虽然消费者取走了消息，但是没有发送确认
    # 给RabbitMQ，所以四个消息会被重新发送到队列中，这样下去会占用内存。
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)

channel.basic_consume(callback,
    queue='task_queue1')

channel.start_consuming()