input_val = input("Enter a string: ")
print(input_val[0] + input_val[1:-1].lower() + input_val[-1])

print(int(len(input_val)/2))

first_half = input_val[0:int(len(input_val)/2)]
sec_half = input_val[int(len(input_val)/2):]
print(first_half[::-1] + "-" + sec_half[::-1])