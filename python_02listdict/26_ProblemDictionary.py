f1 = open("problem1.txt")
f2 = open("problem2.txt")

file1 = f1.readlines()
file2 = f2.readlines()

f1.close()
f2.close()

outputDict = {}
deptDict = {}
values = []

for content in file1:
    deptId = content.split("-")[2]
    name = content.split("-")[1]
    empId = content.split("-")[0]
    city = content.split("-")[3].strip()
    outputDict[empId] = [deptId, name, city]

print(outputDict) 
   
for content in file2:
    deptId = content.split()[0]
    deptName = content.split()[1].strip()
    deptDict[deptId] = deptName
 
print(deptDict)

empId = input("Enter emp ID : ")

try:
    if empId in outputDict:
        print("Name :", outputDict[empId][1])
        print("Location :", outputDict[empId][2])
        print("Department :", deptDict[outputDict[empId][0]])
    else:
        raise Exception("Emp Id not found. Please contact Arpit Kaushik")

except Exception as e:
    print("Arpit Kaushik says : ", e)
