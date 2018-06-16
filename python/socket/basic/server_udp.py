import socket
import sys

bind_ip = "0.0.0.0"
bind_port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((bind_ip,bind_port))

print >>sys.stderr, "[*] Binding on %s:%d (udp)" % (bind_ip, bind_port)


while True:
    
    messages = "Hello, I'm udp server, accept something from you\r\n"
    
    data, addr = server.recvfrom(4096)
    
    print >>sys.stderr, "From: %s:%d\r\nContents: %s(%s bytes)" % (addr[0], addr[1], data, len(data))
    
    server.sendto(messages, addr)
    
    print >>sys.stderr, "sent %s bytes back" % len(messages)
    