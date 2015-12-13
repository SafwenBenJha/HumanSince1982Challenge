import socket
import time
from ip_adress import IPadress
server_socket = socket.socket()
server_name = IPadress
server_port = 149
server_socket.bind((server_name,server_port))
server_socket.listen(10)

while True:

    c , adress = server_socket.accept()
    print "We got connection from", adress
    
    recv = str(c.recv(1024))
    if  recv == "request_A" :
    	c.send("command executed succefully")
    elif recv == "request_B":
    	c.send("error in command execution")
    else: 
    	c.send("server error")
    time.sleep(2)
    c.close()

