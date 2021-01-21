#class Emp(object): #Applicable in Python2.7, it means object is instance of class
class Emp:
    def setName(self, n):
        self.name = n

    def getName(self):
        return self.name

    def setDept(self, d):
        self.dept = d

    def getDept(self):
        return self.dept

    def setSalary(self, s):
        self.salary = s

    def getSalary(self):
        return self.salary

eob1 = Emp()

eob1.setName('Vishal')
eob1.setDept('OLS')
eob1.setSalary(10000)

print(eob1.getName())
print(eob1.getDept())
print(eob1.getSalary())
