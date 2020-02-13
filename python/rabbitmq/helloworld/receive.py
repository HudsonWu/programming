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

# 定义callback函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# 接收消息
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

# 等待接收消息
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
