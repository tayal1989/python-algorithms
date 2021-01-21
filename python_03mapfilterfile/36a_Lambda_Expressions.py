# lambda argument_list:expression
f = lambda x:x*x
print(f(10))

f = lambda x,y:x*y
print(f(10,7))

f = lambda x,y:x*y
# These are keyword arguments, i.e. we are using parameter variables during function calling
# Default arguments are allocated during function definition
print(f(x = 2, y = 3))

f = lambda x=1,y=7:x*y
# These are keyword arguments, i.e. we are using parameter variables during function calling
# Default arguments are allocated during function definition
print(f())

f = lambda x=1,y=7:x*y
# These are keyword arguments, i.e. we are using parameter variables during function calling
# Default arguments are allocated during function definition. This example will use both
# default as well as keyword argument. When keyword argument is given, default argument gets
# over-rided
print(f(x = 7, y = 3))

# Create lambda that will return True if it is even else False
f = lambda x:x%2==0
print(f(10))

f = lambda x:x%2==0
print(f(1))

# Create lambda that will return Yes if it is even else No
f = lambda x:'Yes' if x%2==0 else 'No'
print(f(10))

f = lambda x:'Yes' if x%2==0 else 'No'
print(f(11))
