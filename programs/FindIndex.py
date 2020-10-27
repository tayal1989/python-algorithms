'''
Created on 27-Oct-2020

@author: agarwal.vishal
'''

input_str = "My name is Vishal Agarwal"
input_word = "Vishal"
output_str = ""
count = 0

if len(input_word) > len(input_str):
    return -1

if len(input_str) == 0 and len(input_word) == 0:
    return -1

for i in range(len(input_str)):
    output_str = output_str + input_str[i]
    if(output_str[count] == input_word[count]):
        count = count + 1
        if(count == len(input_word) - 1):
            flag = True
            print("Index Position :", i - len(input_word) + 1 + 1)
            break
    else:
        output_str = ""
        count = 0

if(flag):
    print("Word found")
else:
    print("Word not found")