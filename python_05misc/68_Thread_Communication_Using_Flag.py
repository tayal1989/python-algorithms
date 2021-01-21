'''
Created on Feb 24, 2019

@author: TFPW1884
'''

from threading import Thread
from time import sleep

class Producer:
    
    def __init__(self):
        self.products_list = []
        self.orders_placed = False
        
    def produce(self):
        for i in range(1, 5):
            self.products_list.append("Product" + str(i))
            sleep(1)
            print("Item added")
        self.orders_placed = True

class Consumer:
    
    def __init__(self, prod):
        self.prod = prod
        
    def consume(self):
        while self.prod.orders_placed == False :
            print("Waiting for the orders")
            sleep(0.2)
            
        print("Orders shipped", self.prod.products_list)
        
p = Producer()
c = Consumer(p)

t1 = Thread(target=p.produce)
t2 = Thread(target=c.consume)

t1.start()
t2.start()