import requests
from subprocess import Popen, PIPE, STDOUT
import socket
import time
from ip_adress import IPadress

client_socket = socket.socket()
server_address = IPadress
server_port = 149
cmd1 = 'mkdir new_Human1'
cmd2 = 'rmdir new_Human1'
output =""
task_selected=0
checking_period = 2 #in seconds

def request_A():
    client_socket.connect((server_address,server_port))
    client_socket.send("request_A")
    print client_socket.recv(1024)

def request_B():
    client_socket.connect((server_address,server_port))
    client_socket.send("request_B")
    print client_socket.recv(1024)


while task_selected==0:
    output =""
    p = Popen('ls -l', shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output = p.stdout.read()
    task = raw_input('Would you like to start command 1 or command 2')
    if (task== "1"):
            p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
            output = p1.stdout.read()
            task_selected=1
            print output

    elif (task== "2"):
            p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
            output = p2.stdout.read()
            task_selected=1
            print output

    else:
        print "wrong input"
    time.sleep(checking_period) 
           
if output=="" :
    request_A()
else:
    request_B()



    

