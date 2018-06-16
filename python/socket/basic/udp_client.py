import socket
import sys

target_host = "127.0.0.1"
target_port = 1234
messages = "this is client, transfer something with you\r\n"

# build a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    
    # send some datas
    client.sendto(messages, (target_host, target_port))
    
    print >>sys.stderr, "send %s bytes to %s:%d" % (len(messages), target_host, target_port)
    
    # accept some datas
    data, addr = client.recvfrom(4096)
    
    print "From: %s:%d\r\nGet: %s(%s bytes)" % (addr[0], addr[1], data, len(\
        data))

finally:
    
    print >>sys.stderr, 'closing socket'
    client.close()