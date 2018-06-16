#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

target_host = "www.baidu.com"
target_port = 80

# build a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
client.connect((target_host,target_port))

# send some datas
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

# accept some datas
response = client.recv(4096)

print response

