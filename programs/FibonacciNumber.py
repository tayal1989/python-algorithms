'''
Created on 27-Oct-2020

@author: agarwal.vishal
'''

#0,1,1,2,3,5,8,13,21

f = 0
s = 1

inputUser = input("Enter for how many numbers :")

if(int(inputUser) <= 0):
    print(0)
else:
    print(0,1)
    for i in range(2, int(inputUser)):
        f = f + s
        print(f)
        f, s = s, f