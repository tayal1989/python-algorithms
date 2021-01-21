arr = [11, 12, 13, 14, 15, 16, 17]

temp = []

for i in arr:
    if i % 2 == 1:
        print(i)

for i in arr:
    if i % 2 == 1:
        temp.append(i)

print(temp)

#List Comprehension - writing code in square bracket to make it a list
temp = [i for i in arr if i % 2 == 1 ]

print(temp)

#Dictionary Comprehension
a = ['north', 'south', 'east', 'west']
b = [10, 20, 30, 40]

zones = {}

for i in range(len(a)) :
    zones[a[i]] = b[i]

print(zones)

zones = {a[i]:b[i]  for i in range(len(a))}

print(zones)

zones = {b[i]:a[i]  for i in range(len(a))}

print(zones)
