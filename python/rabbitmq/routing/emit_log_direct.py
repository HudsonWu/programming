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

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)

print(" [x] Sent %r: %r" % (severity, message))

# 关闭连接
connection.close()
