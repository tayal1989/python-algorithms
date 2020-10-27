'''
Created on 27-Oct-2020

@author: agarwal.vishal
'''

input_str = "abcaaabbdc"

outputDict = {}

for i in range(len(input_str)):
    if input_str[i] in outputDict:
        outputDict[input_str[i]] = int(outputDict[input_str[i]]) + 1
    else:
        outputDict[input_str[i]] = 1

print(outputDict)