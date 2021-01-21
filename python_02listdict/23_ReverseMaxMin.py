'''
1) Declare a empty list named "values"
2) Design a for loop which repeats for 6 times
   Prompt the user to enter the data from keyword and store them into the empty list
3) Outside the loop
    a = first_half_of_array
    b = second_half_of_array
4) Print a contents
         b contents - should be reverse
         max = using sort
         min = using sort
'''

def exercise():
    values = []
    for i in range(6):
        i = input("Enter input : ")
        values.append(int(i))

    mid = len(values)/2
    mid = int(mid)

    a = []
    for i in range(mid):
        a.append(int(values[i]))

    print(list(a))
        
    b = []
    for i in range(mid, len(values)):
        b.append(int(values[i]))

    b = list(b)
    print(b)

    b.reverse()

    print("Reverse : ", b)
    print("Max : ", max(values))
    print("Min : ", min(values))
    
exercise()


values = []

for i in range(6):
    number = input("Enter no :")
    values.append(int(number))
    
print(values)
a = values[:3]
b = values[3:]
print(a)
print(b[::-1])
values.sort()
print(max(values))
print(min(values))