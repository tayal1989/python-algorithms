# If all methods in a parent class are abstract methods, then that class is called
# Interface

from abc import abstractmethod, ABCMeta     # Python 2.7
# from abc import abstractmethod, ABC       # Python 3+

# class BMW(object):    #When Using Super() keyword
class BMW:  # When using simple way i.e. ClassName.__init__(self)
# class BMW(ABC):
    __metaclass__ = ABCMeta     # For Python 2.7
    
    def __init__(self, model, year):
        self.model = model
        self.year = year

    @abstractmethod 
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):
    def __init__(self, facility, model, year):
        BMW.__init__(self, model, year)
        self.facility = facility

    def display(self):
        print(self.facility)

    def start(self):
        print("Button Started Car")

    def stop(self):
        print("Interface stop Three Series")

    def drive(self):
        print("Driving at 100km/hr")

class FiveSeries(BMW):
    def __init__(self, anthr_facility, model, year):
        BMW.__init__(self, model, year)
        # Another way of using super class constructor is using keyword super()
        # super(FiveSeries, self).__init__(model, year)
        self.anthr_facility = anthr_facility

    def start(self):
        # If we want to use parent class method functionality
        # super(FiveSeries, self).start()
        print("Remote Started Car")

    def stop(self):
        print("Interface stop Five Series")

    def drive(self):
        print("Driving at 150km/hr")

b = ThreeSeries('faadu', '328i', 2018)
print(b.facility)
print(b.display())
# Accessing parent class variables
print(b.model)
print(b.year)
# Accessing parent class methods
print(b.start())
print(b.stop())

f = FiveSeries('bohat jyada faadu', '528i', 2019)
print(f.anthr_facility)
print(f.model)
print(f.year)
print(f.start())
