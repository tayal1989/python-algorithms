import sys

input_str = "10 abc 10 abc"
input_str = input_str.split()
print "Splitted string : ", input_str
output_str = []
for i in input_str:
    if i not in output_str:
        output_str.append(i)
print "Final Output after removing duplicates : ", output_str

input_str = "10 abc 10 abc"
input_str = input_str.split()
print "Splitted string : ", input_str
print "Final Output after removing duplicates : ", list(set(input_str))

print sys.argv[0]
print sys.argv
