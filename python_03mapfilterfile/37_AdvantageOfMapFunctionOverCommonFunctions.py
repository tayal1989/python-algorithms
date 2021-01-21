#Design a function which accepts one name at a time & return expected result
def get(anyname):
    return anyname[0] + anyname[-1]

arr = ['anil', 'amit', 'sunil', 'hari']

for i in arr:
    res = get(i)
    print(res)

#Problem with this approach is function will be called len(arr) times and it can be executed 
#serially only
#To avoid this prob, we have to use map function

#Map is a class in Python3.5 and map is a function in Python2.7
#Map is a generator function in Python3.5 and map is a normal function in Python2.7
arr = ['anil', 'amit', 'sunil', 'hari']

#list = map(function_name, list)
res = map(get, arr)
print(list(res))    #Yield all approach
