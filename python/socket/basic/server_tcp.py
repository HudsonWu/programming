import socket
import threading
import sys

bind_ip = "0.0.0.0"
bind_port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print >>sys.stderr, "[*] Listening on %s:%d" % (bind_ip, bind_port)

# threading
def handle_client(client_socket):
    
    # print contents from client
    request = client_socket.recv(1024)
    
    print >>sys.stderr, "[*] Received: %s(%s bytes)" % (request, len(request))
    
    # returns a packet
    messages = "Hello, this is server, you get a ACK!"
    client_socket.send(messages)
    print >>sys.stderr, "sent %s bytes back" % len(messages)
    client_socket.close()

while True:
    
    client, addr = server.accept()
    
    print >>sys.stderr, "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
    
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
    