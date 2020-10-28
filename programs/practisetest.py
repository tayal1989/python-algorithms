'''
Created on 27-Oct-2020

@author: agarwal.vishal
'''

def upper_function(function):
    def inner_function():
        func = function()
        output_str = func.upper()
        return output_str
    return inner_function

def upper_split_function(function):
    def inner_split_function():
        func = function()
        output_str = func.split()
        return output_str
    return inner_split_function
    
@upper_split_function
@upper_function
def print_function():
    return "hello world"

print(print_function())