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

# 创建一个exchange, 命名为direct_logs
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)

# 定义callback函数
def callback(ch, method, properties, body):
    print(" [x] %r: %r" % (method.routing_key, body))
    print(" [x] Done")

# 接收消息
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback, auto_ack=True)

# 等待接收消息
print(' [*] Waiting for logs. To exit press CTRL+C')
channel.start_consuming()
