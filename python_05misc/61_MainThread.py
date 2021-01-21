'''
Created on Feb 24, 2019

@author: TFPW1884
'''

'''
Three ways to create a new thread apart from main() thread
1. Using function
   t = Thread(target=function_name, args)
   t.start()
   
2. Extending the thread class
   class MyThread(Thread):
   override the run()
   t.start()
   
3. Without extending Thread class
    class MyThread
        display()
        
    t = Thread(target=myobj.display, args)
'''

import threading

print("Current Thread i.e running :", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("Main Thread")
else:
    print("Other Thread")