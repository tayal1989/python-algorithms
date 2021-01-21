# Decorators takes a function as an argument and returns a function as a result
# But a function that is returned by the decorator performs additional processing
# of the function that is given as an argument

def decor(fun, y):
    def inner(x):
        result = fun * x
        return result * 2
    return inner(y)

def num(no):
    return no

result = decor(num(5), 4)
print(result)

# Another way of using decorator i.e. using '@' operator

def another_decor(fun):
    def another_inner(value):
        result = fun(value)
        return result * 2
    print("Inside decorator :", another_inner(4))
    return another_inner

@another_decor
def another_num(y):
    return y

print(another_num(6))
