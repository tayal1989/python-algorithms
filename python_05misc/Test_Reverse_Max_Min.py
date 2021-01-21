values = []
for i in range(6):
    i = input("Enter val :")
    values.append(int(i))
print values

a = values[0:len(values)/2]
print a
b = values[len(values)/2:]
print b
b.reverse()
print "Reverse of b : ", b
print "Maximum : ", max(values)
print "Minimum : ", min(values)
