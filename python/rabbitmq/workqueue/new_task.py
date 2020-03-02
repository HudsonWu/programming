#!/usr/bin/env python3

import pika
import sys

# 与broker连接所需验证信息
credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
parameters = pika.ConnectionParameters('192.168.19.45',
                                       5672,
                                       '/',
                                       credentials)

# 与broker建立连接
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# 创建一个queue
channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))

print(" [x] Sent %r" % message)

# 关闭连接
connection.close()
