'''
Created on Feb 24, 2019

@author: TFPW1884
'''
from threading import Thread


class BookMyBus:
    
    def buy(self):
        print("Confirming a seat")
        print("Processing Payment")
        print("Printing the ticket")


bmb = BookMyBus()
t1 = Thread(target=bmb.buy)
t2 = Thread(target=bmb.buy)
t3 = Thread(target=bmb.buy)

t1.start()
t2.start()
t3.start()