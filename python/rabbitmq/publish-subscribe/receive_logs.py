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

# 创建一个exchange, 命名为logs
channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='logs', queue=queue_name)

# 定义callback函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    print(" [x] Done")

# 接收消息
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback, auto_ack=True)

# 等待接收消息
print(' [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()
