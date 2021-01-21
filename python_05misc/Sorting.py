input_list = [8, 6, 2, 3]
#input_list.sort()
print "List : ", input_list

for i in range(len(input_list) - 1):
    for j in range(len(input_list) - 1 - i):
        if input_list[j + 1] < input_list[j]:
            input_list[j + 1], input_list[j] = input_list[j], input_list[j + 1] # Swapping
        j = j + 1
    i = i + 1

print "Sorted List : ", input_list
