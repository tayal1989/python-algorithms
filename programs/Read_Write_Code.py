def read_approach_1():
    f = open("Read_Write_File.txt")
    contents = f.read()
    print(contents)
    print(type(contents))
    f.close()

# read_approach_1()

def read_approach_2():
    f = open("Read_Write_File.txt")
    val = ''
    line = f.readline()
    print("Outside loop :", line)
    while line != "" :
        line = f.readline()
        #val = val + line
        print("Inside loop :", line)
    f.close()

# read_approach_2()

def read_approach_3():
    f = open("Read_Write_File.txt")
    lines = f.readlines()
    print(lines)
    contents = ''
    for line in lines:
        contents = contents + line
    print(contents)
    print(type(lines))
    f.close()

# read_approach_3()

def read_approach_4():
    f = open("Read_Write_File.txt")
    lines = f.readlines()
    print(lines)
    print(type(lines))
    for line in lines:
        print(line)
    f.close()

# read_approach_4()

def read_approach_5():
    f = open("Read_Write_File.txt")
    for line in f:
        print(line,)
        print(type(line))
    f.close()

# read_approach_5()

def write_approach_1():
    f = open("Read_Write_File.txt", 'r')
    lines = f.readlines()
    contents = ''
    for line in lines:
        contents = contents + line
    f.close()
    f = open("Write_File.txt", 'w')
    f.write(contents)
    f.close()

#write_approach_1()

#read_approach_3()
