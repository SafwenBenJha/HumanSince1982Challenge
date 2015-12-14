import requests
from subprocess import Popen, PIPE, STDOUT
import time
from ip_adress import IPadress

#IPadress = "127.0.0.1"
port = "8080"
cmd1 = 'mkdir new_Human1'
cmd2 = 'rmdir new_Human1'
output =""
task_selected=0
checking_period = 1 #in seconds

def request_A():
    response = requests.get("http://" + IPadress + ":" + port + "/since1982")  
    jsonObj = response.json()
    print "FirstName is " + str(jsonObj["humans"][0]["name"])
def request_B():
    response = requests.get("http://" + IPadress + ":" + port + "/since1982")
    jsonObj = response.json()
    print "LastName is " + str(jsonObj["humans"][1]["name"])

while True:
    time.sleep(checking_period)
    task_selected=0;
    output =""
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
               
    if output=="" and task_selected==1:    
        request_A()
    elif task_selected==1:
        request_B()


