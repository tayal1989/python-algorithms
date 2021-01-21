'''
Created on Feb 17, 2019

@author: TFPW1884
'''

l = [1, 3, 7, 2, 4]
i = 0
out_sum = 7
while i < len(l):
    diff_of_no = out_sum - l[i]
    if diff_of_no in l:
        other_no_index = l.index(diff_of_no)
        print(l[i], l[other_no_index])
    i += 1
