#class Emp(object): #Applicable in Python2.7, it means object is instance of class
class Emp:

    counter = 0
    
    #Default constructor in Python
    def __init__(self, name = None, dept = None, salary = None):         #self is The first argument of every class method,
                                                                         #including __init__, is always a reference to the current instance of the class.
                                                                         #By convention, this argument is always named self.
                                                                         #In the __init__ method, self refers to the newly created object;
                                                                         #in other class methods, it refers to the instance whose method was called
        self.name = name
        self.dept = dept
        self.salary = salary
        Emp.counter+=1

    #Destructor in Python. It will be used when you open a file in default constructor then you can close the file here in destructor
    #The destructor value will show in command line not in IDE as IDE will handle the garbage collector so it doesn't print any thing
    #however, in command line, it has to do all the things
    def __del__(self):
        print("I am in destructor")
        Emp.counter-=1
        print("In Destructor : ", Emp.counter)
        self = None

    def showvalues(self):
        print(self.name)
        print(self.dept)
        print(self.salary)

    @staticmethod
    def showcounter():
        print("Counter = ", Emp.counter)

eob1 = Emp('amit', 'sales', 15000)
eob2 = Emp('hari', 'hrd', 10000)
eob3 = Emp()
eob1.showvalues()
eob2.showvalues()
eob3.showvalues()

print(Emp.showcounter())

print(type(eob1))
print(eob1)

print(eob1.__dict__)
print(eob1.showvalues)
print(eob1.showcounter)