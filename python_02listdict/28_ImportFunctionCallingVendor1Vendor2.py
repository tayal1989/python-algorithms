#import Vendor1   #If file to be imported is in the current folder of the file to be executed
#import Vendor2   #If file to be imported is in the current folder of the file to be executed

#import MyPack.Vendor1
#import MyPack.Vendor2

#If I want to import multiple files from MyPack directory
from MyPack import *

print(dir(Vendor1))
print(dir(Vendor2))

#print(dir(MyPack.Vendor1))
#print(dir(MyPack.Vendor2))


Vendor1.init()
Vendor1.clean()

Vendor2.start()
Vendor2.clean()
'''

MyPack.Vendor1.init()
MyPack.Vendor1.clean()

MyPack.Vendor2.start()
MyPack.Vendor2.clean()
'''
