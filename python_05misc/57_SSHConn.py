#Importing modules
import paramiko
import sys
import time

#setting parameters like host IP, username, passwd and number of iterations to gather cmds
HOST = "10.43.13.54"
USER = "tester"
PASS = "tester"


#A function that logins and execute commands
def fn():
  client1=paramiko.SSHClient()
  #Add missing client key
  client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  #connect to switch
  client1.connect(HOST,username=USER,password=PASS)
  print "SSH connection to %s established" %HOST
  #Gather commands and read the output from stdout
  stdin, stdout, stderr = client1.exec_command('ls\n')
  print stdout.read()
  client1.close()
  print "Logged out of device %s" %HOST

fn()
