x = 123

def sample_func():
    x = 456
    print(x)
    print(globals()['x'])

print(sample_func())
z=sample_func
print(z())
