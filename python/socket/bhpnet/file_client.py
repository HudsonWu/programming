#!/usr/bin/env python

import socket, sys

address = ("127.0.0.1", 1234)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(address)

read_file = open("/home/hudson/haha.txt", "rb")
data = read_file.read(1024)

while data:
    client.send(data)
    data = read_file.read(1024)
