#telnet username : toor4nsn
#telnet password : oZPS0POrRieRtu

import getpass
import sys
import telnetlib
from time import sleep


HOST = "192.168.255.131"
user = raw_input("Enter your remote account: ")
password = raw_input("Enter your remote password: ")
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(user + "\n")
if password:
   tn.read_until("Password: ")
   tn.write(password + "\n")

#tn.write("vt100\n")
sleep(2)
tn.write("pwd\n")
sleep(2)
#tn.write("telnet 192.168.254.1 200\n")
#sleep(2)
#tn.write("FRMon\n")
#sleep(2)
tn.write("exit\n")
print tn.read_all()