'''
Created on Feb 24, 2019

@author: TFPW1884
'''

from threading import Thread #, Semaphore
from threading import Lock

class BookMyBus:
    
    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.l = Lock() # 1st way of acquiring lock
        # self.l = Semaphore() # 2nd way of acquiring lock
    
    def buy(self, seats_requested):
        self.l.acquire()
        print("Total seats available : ", self.available_seats)
        if self.available_seats >= seats_requested :
            print("Confirming a seat")
            print("Processing Payment")
            print("Printing the ticket")
            self.available_seats -= seats_requested
        else:
            print("Sorry, no seats available")
        self.l.release()


bmb = BookMyBus(10)
t1 = Thread(target=bmb.buy, args=(3,)) # args must be list or iterator, therefore, used comma
t2 = Thread(target=bmb.buy, args=(2,))
t3 = Thread(target=bmb.buy, args=(4,))

t1.start()
t2.start()
t3.start()