'''
Created on 22-Oct-2020

@author: agarwal.vishal
'''

def count_collect_vowels(input_string):
    no_of_vowels = 0
    output_string = ''
    for char in input_string:
        if char in 'aeiouAEIOU':
            no_of_vowels = no_of_vowels + 1
            output_string = output_string + char
    
    print("No of vowels : ", no_of_vowels)
    print("Vowels : ", output_string)        

count_collect_vowels("Vishal")