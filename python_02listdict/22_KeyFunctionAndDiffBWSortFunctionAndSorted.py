studs = [
    'arun-CSE-67',
    'hari-CSE-74',
    'john-ISE-65',
    'ajit-CSE-54',
    'manu-ISE-76',
    'elan-CSE-65',
    'balu-ISE-85',
    'amar-CSE-87'
    ]

#Sort them
studs.sort()

print(studs)
print("\n".join(studs))		#Sort on basis of names, first ajit will come and at last manu will come

print("\n")

#Sort them in reverse
studs.sort(reverse=True)

print("\n".join(studs))		#Reverse Sort on basis of names, first manu will come and at last ajit will come

print("\n")

#Key is based on what parameter, sort operation needs to be performed
studs.sort(key = lambda x:x.split("-")[1],reverse=False)

print("\n".join(studs))		#Sort on basis of branch, first CSE will come and at last ISE will come

print("\n")

studs.sort(key = lambda x:int(x.split("-")[2]),reverse=True)

print("\n".join(studs))
print("\n")			#Reverse Sort on basis of marks, first 87 will come and at last 54 will com

#Sort by department and then by marks
def fun(x):
    name, dept, marks = x.split("-")
    return dept, -int(marks)    # To print marks in reverse order for the particular department use "-" in front of int(marks)

studs.sort(key=fun, reverse=True)

print("\n".join(studs))
print("\n")

studs.sort(key=fun)

print("\n".join(studs))
print("\n")

arr = [4,2,6,1]

#Difference between sort function and sorted is once list is sorted using list.sort(), it will remain sorted. However, using sorted() function, it can be used when it is required and then when you print list, it will not show in sorted manner.
print(sorted(arr))
print(arr)
arr.sort()
print(arr)

#Similary it works for reverse
#arr.reverse()
#res = reversed(arr)
