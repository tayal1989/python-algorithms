#Reduce is used as a recursive function and the return type is not a list, it will return as integer
#Within reduce, lambda expects two arguments while in map and filter lambda expects one argument

from functools import reduce

arr = range(1, 6)

res = reduce(lambda x,y : x + y, arr)

print(res)
