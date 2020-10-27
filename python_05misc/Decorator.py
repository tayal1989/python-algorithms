import time

def deco(func):
    def wrapper(*args, **kwargs):
        s = time.time()
        result = func(*args, **kwargs)
        e = time.time()
        print func.__name__ + " took " + str((e - s)) + " mil sec"
        return result
    return wrapper

@deco
def square_of_number(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result

@deco
def cube_of_number(numbers):
    result = []
    for number in numbers:
        result.append(number * number * number)
    return result

array = range(1, 10)
print square_of_number(array)
print cube_of_number(array)
    
