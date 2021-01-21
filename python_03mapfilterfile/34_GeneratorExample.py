'''
This program will tell the difference between normal function and generator & iterator
'''

def first_fun():
    print("Hi")
    return 1
    return 2

def generator_fun():
    '''
    Once it finds yield, control transfer to the main block by preserving the current statement
    '''
    print("Hi")
    yield 1
    yield 2
    #return 1
    yield "Three"

res = first_fun()
print(res)

res = generator_fun()
print(res.__next__())
print(res.__next__())

arr = list(generator_fun())
print(arr)

print("\n")

res = range(1, 11)
print(list(res))

name = 'vishal'
# C loop
for i in range(len(name)):
    print(i, " = ", name[i])

print

# Java loop
for index, value in enumerate(name):
    print(index, " = ", value)

print

# C++ loop
for i in name:
    print(i)