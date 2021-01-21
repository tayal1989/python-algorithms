#class Emp(object): #Applicable in Python2.7, it means object is instance of class
class Car:    
    #Default constructor in Python
    def __init__(self, make, year):
        self.make = make
        self.year = year

    class Engine:
        def __init__(self, unique_no):
            self.unique_no = unique_no

        def start_engine(self):
            print("Started Engine")

c = Car("BMW", 2019)
# To access Engine class, we have to use object of class Car
e = c.Engine(123)
e.start_engine()
