fob = open("one.txt", "w")

fob.write("10\n20\n30\n40\n50")
fob.close()

fob = open("FileCreationOutput.txt")
#print(fob.read())

for i in fob:
    i = i.strip()   # To remove extra \n
    print(i)
fob.close()
#print(fob)

