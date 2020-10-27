'''
Created on 26-Oct-2020

@author: agarwal.vishal
'''
studs = ['ravi 10,20,30,40,50,6',
         'hari 5,40,10,30,20,45',
         'ramu 10,20,30,40,50,6',
         'ajit 5,40,10,30,20,45'
         ]

marks = []
for i in studs:
    marks = i.split()[1]
    mark = []
    value = marks.split(",")
    print(value)
    for j in value:
        mark.append(int(j))
    print("Total sum :", sum(mark))
    print("Max mark :", max(mark))