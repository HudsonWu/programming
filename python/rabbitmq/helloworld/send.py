#!/usr/bin/env python3

import pika

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
channel.queue_declare(queue='hello')

# 发送message
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body= 'hello, I am a python testing application')

print(" [x] Sent 'Hello World!'")

# 关闭连接
connection.close()
