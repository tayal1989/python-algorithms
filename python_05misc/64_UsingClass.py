'''
Created on Feb 24, 2019

@author: TFPW1884
'''
from threading import Thread
from threading import current_thread
from time import sleep


class MyThread:
    def display_numbers(self):
        i = 0
        print("Current Thread : ", current_thread().getName())
        sleep(1)
        while i <= 10:
            print(i)
            i += 1

object_of_class = MyThread()

# Applying multi-threading by creating multiple objects
t1 = Thread(target=object_of_class.display_numbers)
t1.start()

t2 = Thread(target=object_of_class.display_numbers)
t2.start()

t3 = Thread(target=object_of_class.display_numbers)
t3.start()
