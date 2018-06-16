#!/usr/bin/env python

import sys, socket, getopt, threading, subprocess

# global variable
listen = False
command = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print "BHP Net Tool"
    print
    print "Usage: bhpnet.py -t target_host -p port"
    print "-l --listen                 - listen on [host]:[port] for\r\n\
                                         incoming connections"
    print "-e --execute=file_to_run    - execute the given file upon\r\n\
                                         receiving a connection"
    print "-c --command                - initialize a command shell"
    print "-u --upload=destination     - upload receiving connection\r\n\
                                         upload a file and write to [destination]"
    print
    print "Example: "
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u \"c:\\target.exe\""
    print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e \"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 1234"
    sys.exit(0)

def client_sender(buffer):
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        
        # connet to target host
        client.connect((target,port))
        
        if len(buffer):
            client.send(buffer)
        
        while True:
            # wait data return
            recv_len = 1
            response = ""
            
            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                
                if recv_len < 4096:
                    break
                
            print response,
            
            # wait more input
            buffer = raw_input("")
            buffer += "\n"
            
            # send to
            client.send(buffer)
    except:
        
        print "[*] Exception! Exiting."
        client.close()
            

def server_loop():
    
    global target
    
    # if no target, listen all
    if not len(target):
        target = "0.0.0.0"
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    
    server.listen(5)
    
    while True:
        client_socket, addr = server.accept()
        
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()
    
def run_command(command):
    
    # a new line
    command = command.rstrip()
    # run command and return output
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "Failed to execute command.\r\n"
        
    # send the output
    return output
    

def client_handler(client_socket):
    global upload_destination
    global execute
    global command
    
    # detect upload file
    if len(upload_destination):
        
        print >>sys.stderr, "upload_destination is %s" % upload_destination
        
        # read all characters and write destination
        file_buffer = ""
        
        # read datas until no valid datas
        data = client_socket.recv(1024)
        while data:
            
            file_buffer += data
            data = client_socket.recv(1024)
            
        
        # write datas
        try:
            file_descriptor = open(upload_destination, "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()
            
            # confirm file write success
            client_socket.send("Successfully saved file to %s\r\n" % upload_destination)
            client_socket.close()
        except:
            client_socket.send("Failed to save file to %s\r\n" % upload_destination)
            client_socket.close()
    
    # check command execute
    if len(execute):
        # run command
        output = run_command(execute)
        
        client_socket.send(output)
        client_socket.close()
        
    # if command line shell
    if command:
        while True:
            # Jump out of a window
            client_socket.send("<BHP:#> ")
            
            # accept file until enter key
            cmd_buffer = ""
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
                
            # back command output
            response = run_command(cmd_buffer)
            # back response datas
            client_socket.send(response)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target
    
    if not len(sys.argv[1:]):
        usage()
    
    # read option
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",\
            ["help", "listen", "execute", "target", "port", "command", "upload"])
        print >>sys.stderr, "-- opts=%s --" % str(opts)
        print >>sys.stderr, "-- args=%s --" % str(args)
    except getopt.GetoptError as err:
        print str(err)
        usage()
    
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "Unhandled Option"
    
    if not listen and len(target) and port > 0:
        
        # Read memory data from command line
        buffer = sys.stdin.read()
        
        # send datas
        # if blocking, CTRL+D
        client_sender(buffer)
        
    # Start to listen and ready to upload files, execute commands
    # place the rebound shell
    if listen:
        server_loop()
        
main()