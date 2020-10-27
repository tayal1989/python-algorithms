with open("CountWordsInFile.txt", "r") as f:
    file1 = f.readlines()
    
outputDict = {}

for lines in file1:
    line = lines.split()
    for word in line:
        if word in outputDict:
            outputDict[word] = int(outputDict[word]) + 1
        else:
            outputDict[word] = 1

print(outputDict)