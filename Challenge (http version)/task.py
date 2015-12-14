import requests
from subprocess import Popen, PIPE, STDOUT
import time
from ip_adress import IPadress

#IPadress = "127.0.0.1"
port = "8080"
cmd1 = 'mkdir new_Human1'
cmd2 = 'rmdir new_Human1'
task_selected=0
checking_period = 1 #in seconds
url = "http://" + IPadress + ":" + port + "/since1982"

def request_A():
    response = requests.get(url)  
    jsonObj = response.json()
    print "Received Command is " + str(jsonObj["humans"][0]["name"])
def request_B():
    response = requests.get(url)
    jsonObj = response.json()
    print "Received Command is " + str(jsonObj["humans"][1]["name"])

while True:
    time.sleep(checking_period)
    task_selected=0; #init to 0
    output =""  #init to empty string
    #get input from keyboard to select a scenario (task) to launch request A or B
    task = raw_input('Would you like to start command 1 or command 2')
    if (task== "1"):
            #execute command shell
            p1 = Popen(cmd1, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
            output = p1.stdout.read()
            task_selected=1
            print output

    elif (task== "2"):
            #execute command shell
            p2 = Popen(cmd2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
            output = p2.stdout.read()
            task_selected=1
            print output
    else:
        print "wrong input"        
               
    if output=="" and task_selected==1:  #if the command was executed correctly withut errors  
        request_A()
    elif task_selected==1: #There was an error in command execution
        request_B()


