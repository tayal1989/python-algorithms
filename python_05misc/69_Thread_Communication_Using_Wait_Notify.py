'''
Created on Feb 24, 2019

@author: TFPW1884
'''

from threading import Thread, Condition
from time import sleep

class Producer:
    
    def __init__(self):
        self.products_list = []
        self.c = Condition()
        
    def produce(self):
        self.c.acquire()
        
        for i in range(1, 5):
            self.products_list.append("Product" + str(i))
            sleep(1)
            print("Item added")
        
        self.c.notify()
        self.c.release()

class Consumer:
    
    def __init__(self, prod):
        self.prod = prod
        
    def consume(self):
        self.prod.c.acquire()
        self.prod.c.wait(timeout = 0)   # After it gets notified, how much time it has to wait
        self.prod.c.release()
        print("Orders shipped", self.prod.products_list)


p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()