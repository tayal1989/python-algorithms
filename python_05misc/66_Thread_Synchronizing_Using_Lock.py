'''
Created on Feb 24, 2019

@author: TFPW1884
'''

'''
There is a problem with this code i.e. if thread 1 is confirming and
booking a ticket, thread 2 can come and start booking the same ticket
or try to book tickets even if seats are not available.
So to overcome this defect, kindly use acquire and release code
explained in next file
'''

from threading import Thread


class BookMyBus:
    
    def __init__(self, available_seats):
        self.available_seats = available_seats
    
    def buy(self, seats_requested):
        print("Total seats available : ", self.available_seats)
        if self.available_seats >= seats_requested :
            print("Confirming a seat")
            print("Processing Payment")
            print("Printing the ticket")
            self.available_seats -= seats_requested
        else:
            print("Sorry, no seats available")


bmb = BookMyBus(10)
t1 = Thread(target=bmb.buy, args=(3,)) # args must be list or iterator, therefore, used comma
t2 = Thread(target=bmb.buy, args=(2,))
t3 = Thread(target=bmb.buy, args=(4,))

t1.start()
t2.start()
t3.start()