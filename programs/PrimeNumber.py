'''
Created on 27-Oct-2020

@author: agarwal.vishal
'''

input_no = input("Enter number :")
sqr_root = int(input_no) ** 0.5
flag = True

for i in range(2, int(sqr_root) + 1):
    if(int(input_no) % i == 0):
        flag = False
        break

if(flag):
    print("Prime Number")
else:
    print("Not Prime")