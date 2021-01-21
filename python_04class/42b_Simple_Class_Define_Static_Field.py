#class Emp(object): #Applicable in Python2.7, it means object is instance of class
class Emp:
    # Static field
    counter = 2
    
    #Default constructor in Python
    def __init__(self):         #self is The first argument of every class method,
                                #including __init__, is always a reference to the current instance of the class.
                                #By convention, this argument is always named self.
                                #In the __init__ method, self refers to the newly created object;
                                #in other class methods, it refers to the instance whose method was called
        self.name = 'Vishal'
        self.dept = 'OLS'
        self.salary = '10000'

eob1 = Emp()
print(eob1.name)
print(eob1.dept)
print(eob1.salary)
print(eob1.counter)

eob2 = Emp()
print(eob2.name)
print(eob2.dept)
print(eob2.salary)
print(eob2.counter)

print(Emp.counter)
