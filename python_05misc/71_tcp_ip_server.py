'''
Created on Feb 24, 2019

@author: TFPW1884
'''

import socket

host = 'localhost'
port = 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

print("Server listening on port : ", port)
s.listen(1)

c, addr = s.accept()

print("Connection From : ", str(addr))

c.send(b"Hello, how are you")
c.send("Bye".encode())
c.close()