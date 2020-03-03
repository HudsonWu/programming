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
channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def on_request(ch, method, props, body):
    n = int(body)
    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                       props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)

# 接收消息
channel.basic_consume(queue='rpc_queue',
                      on_message_callback=on_request)

# 等待接收消息
print(' [*] Awaiting RPC requests. To exit press CTRL+C')
channel.start_consuming()
