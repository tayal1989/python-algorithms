'''
Created on 22-Oct-2020

@author: agarwal.vishal
'''

def find_average(grades):
    averages = []
    for list_of_grades in grades:
        total = 0
        for grade in list_of_grades:
            total = total + grade
        averages.append(total/len(list_of_grades))
    return averages

input_grade = [[70, 75, 80], [70, 80, 90, 100], [80, 100]]
print(find_average(input_grade))