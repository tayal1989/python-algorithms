'''
Created on 22-Oct-2020

@author: agarwal.vishal
'''
def area_of_triangle(base, height):
    """(number, number) -> float
    
    Calculates area of triangle
    
    >>> area_of_triangle(5, 10)
    25
    >>> area_of_triangle(5, 20)
    50
    """
    
    return (1/2 * base * height)

print("In class Sample Function : ", area_of_triangle(4, 2))