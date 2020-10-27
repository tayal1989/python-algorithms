def rev_order_of_word(input_str):
    split_str = input_str.split()
    split_str = split_str[::-1]
    print(" ".join(split_str))

rev_order_of_word('I am a good boy')

input_str = "I am a good boy"
split_str = input_str.split()
split_str = split_str[::-1]
output_str = ""
for i in range(len(split_str)):
    output_str = output_str + split_str[i][::-1] + " "

print(output_str)
print(input_str[::-1])