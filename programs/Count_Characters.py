def count_characters(string1):
    out_str = ''
    count = 0
    ind = 0
    
    while ind < len(string1):
        j = ind + 1
        
        while j < len(string1):
            if string1[ind] == string1[j]:
                count = count + 1
            else:
                break
            j = j + 1
            
        if count > 0:
            out_str = out_str + string1[ind] + str(count)
        else:
            out_str = out_str + string1[ind]
            
        count = 0
        
        if j == len(string1):
            break
        
        ind = j
        
    print(out_str)

count_characters("abcaaabbdc")
count_characters("aaaab")
count_characters("aaaa")
count_characters("abc")
count_characters("aabbc")
count_characters("")

input_str = "abcaaabbdc"

outputDict = {}

for i in range(len(input_str)):
    if input_str[i] in outputDict:
        outputDict[input_str[i]] = int(outputDict[input_str[i]]) + 1
    else:
        outputDict[input_str[i]] = 1

print(outputDict)

