#class Emp(object): #Applicable in Python2.7, it means object is instance of class
class Emp:

    
    #Default constructor in Python
    def __init__(self, name = None, dept = None, salary = None):         #self is The first argument of every class method,
                                                                         #including __init__, is always a reference to the current instance of the class.
                                                                         #By convention, this argument is always named self.
                                                                         #In the __init__ method, self refers to the newly created object;
                                                                         #in other class methods, it refers to the instance whose method was called
        #self.__name = name     #Private member
        self.name = name
        #print(name)
        self.dept = dept
        self.salary = salary

    def showvalues(self):
        #print(self.__name)
        print(self.name)
        print(self.dept)
        print(self.salary)


eob1 = Emp('amit', 'sales', 15000)
#print("Hello = ", eob1.__name)         #we can't access private member outside the class
print("Hello = ", eob1.name)         #we can't access private member outside the class
print(eob1.showvalues())
print(eob1)
#print(_Emp__name)
