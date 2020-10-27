#class Emp(object): #Applicable in Python2.7, it means object is instance of class
class Emp:

    
    #Default constructor in Python
    def __init__(self, name = None, dept = None, salary = None):         #self is The first argument of every class method,
                                                                         #including __init__, is always a reference to the current instance of the class.
                                                                         #By convention, this argument is always named self.
                                                                         #In the __init__ method, self refers to the newly created object;
                                                                         #in other class methods, it refers to the instance whose method was called
        self.__name = name     #Private member
        self.dept = dept
        self.salary = salary

    def showvalues(self):
        print(self.__name)
        print(self.dept)
        print(self.salary)


class Developer(Emp):           #Inheriting the class
    #def __init__(self, manager = None, team = None, project = None):
    def __init__(self, name = None, dept = None, salary = None, manager = None, team = None, project = None):    #If I have to pass base class values also
        #Emp.__init__(self)                  #Work around for constructor cascading
        Emp.__init__(self, name, dept, salary)                  #Work around for constructor cascading to call parameters of parent class
        self.manager = manager
        self.team = team
        self.project = project

    def show(self):
        print("Manager = ", self.manager)
        print("Team = ", self.team)
        print("Project = ", self.project)

    #Treat object like a string
    def __str__(self):
        return "Hi"

    #to compare the parameters of two objects
    def __eq__(self, another):
        return self.dept == another.dept

eob1 = Developer(dept = 'sales')
#print(eob1.show())
print(eob1)
print(eob1._Emp__name)      #To access private members
print(eob1.__dict__)

eob2 = Developer(dept = 'sales')

if eob1 == eob2 :
    print("They work in same dept")
else:
    print("No, they don't work in same diff")