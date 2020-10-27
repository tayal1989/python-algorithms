num = [1, -2, 3, 4, 5]

def square(anyno):
    return anyno * anyno

res = map(square, num)
print(list(res))

res = map(lambda x:x*x, num)
print(res)
