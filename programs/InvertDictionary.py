'''
Created on 23-Oct-2020

@author: agarwal.vishal
'''
fruit_to_colour = {'watermelon': 'green', 'pomegranate': 'red',
'peach': 'orange', 'cherry': 'red', 'pear': 'green',
'banana': 'yellow', 'plum': 'purple', 'orange': 'orange'}

colour_to_fruit = {}
for fruit in fruit_to_colour:
    colour = fruit_to_colour[fruit]
    if colour in colour_to_fruit:
        colour_to_fruit[colour].append(fruit)
    else:
        colour_to_fruit[colour] = [fruit]   # take this value as a list

for colour in colour_to_fruit:
    print(colour, ":", colour_to_fruit[colour])