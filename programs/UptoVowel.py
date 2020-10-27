'''
Created on 22-Oct-2020

@author: agarwal.vishal
'''
def upto_vowel(input_string):
    output_string = ""
    for i in range(len(input_string)):
        if input_string[i] in 'aeiouAEIOU':
            break
        else:
            output_string = output_string + input_string[i]
    return output_string
        
print(upto_vowel("Hello"))
print(upto_vowel("There"))