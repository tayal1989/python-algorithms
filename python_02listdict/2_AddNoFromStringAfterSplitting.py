'''
Created on 27-Oct-2020

@author: agarwal.vishal
'''

studs = ['arun-30',
         'hari-10',
         'mani-44',
         'john-23',
         'kala-34',
         'ravi-11'
         ]

sumOfMarks = 0

for i in studs:
    sumOfMarks = sumOfMarks + int(i.split("-")[1])

print(sumOfMarks)

studs = ['arun', 'hari', 'manu', 'ravi', 'ajit']

for i in studs :
    print(i[0].upper() + i[1:-1] + i[-1].upper())

studs = ['ravi 10,20,30,40,50,6',
         'hari 5,40,10,30,20,45',
         'ramu 10,20,30,40,50,6',
         'ajit 5,40,10,30,20,45'
         ]

for i in studs:
    marks = i.split()[1]
    value = marks.split(",")
    mark = []
    mark[:] = map(int, value)
    print(mark)
    print(sum(mark))
    print(max(mark))