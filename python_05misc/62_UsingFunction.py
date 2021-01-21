'''
Created on Feb 24, 2019

@author: TFPW1884
'''
from threading import current_thread
from threading import Thread

def display_numbers():
    i = 0
    print("Inside thread function : ", current_thread().getName())
    while i <= 10:
        print(i)
        i += 1
        
print(current_thread().getName())
t = Thread(target=display_numbers)
t.start()