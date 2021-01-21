from multiprocessing import Process, Queue, Lock

from threading import Thread
import threading
import os

def job1(q,l):
    l.acquire()
    q.put("Hello world")
    l.release()
    print("Hi in job1 = ", os.getpid(), " = ", threading.current_thread())
    
def job2(q):
    print("Hello in job2 = ", os.getpid(), " = ", threading.current_thread())
    print("Message : ", q.get())

if __name__ == '__main__':
    print("Main started = ", os.getpid())

    q = Queue()
    l = Lock()
    #p1 = Process(target = job1, args = ())
    #p2 = Process(target = job2, args = ())

    p1 = Thread(target = job1, args = (q, l))
    p2 = Thread(target = job2, args = (q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Main ended")
