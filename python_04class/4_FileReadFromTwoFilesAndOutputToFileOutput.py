#MyApproach
fob1 = open("file1.txt", "r")
#print(fob1.readline())
name = []
for i in fob1:
    i = i.strip()
    name.append(i)

print(name)

fob2 = open("file2.txt", "r")
#print(fob2.readline())
marks = []
for i in fob2:
    i = i.strip()
    marks.append(i)

print(marks)

fob = open("fileOutput.txt", "w")

for line in range(0,5):
    val = name[line], "=", marks[line]
    fob.writelines(val)
    fob.writelines("\n")
    #line = line + 1

fob.close()

fob1.close()
fob2.close()


#Teacher Method
fob1 = open("file1.txt")
fob2 = open("file2.txt")

a = fob1.readlines()
b = fob2.readlines()

fob1.close()
fob2.close()

fob3 = open("outteacher.txt", "w")
for i in range(len(a)):
    fob3.write(a[i].strip() + "=" + b[i])

fob3.close()
