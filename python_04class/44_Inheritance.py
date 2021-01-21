class BMW(object):    #When Using Super() keyword
# class BMW:  # When using simple way i.e. ClassName.__init__(self)
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def start(self):
        print("Started Car")

    def stop(self):
        print("Stopped Car")

class ThreeSeries(BMW):
    def __init__(self, facility, model, year):
        BMW.__init__(self, model, year)
        self.facility = facility

    def display(self):
        print(self.facility)

    def start(self):
        print("Button Started Car")

class FiveSeries(BMW):
    def __init__(self, anthr_facility, model, year):
        # BMW.__init__(self, model, year)
        # Another way of using super class constructor is using keyword super()
        super(FiveSeries, self).__init__(model, year)
        self.anthr_facility = anthr_facility

    def start(self):
        # If we want to use parent class method functionality
        super(FiveSeries, self).start()
        print("Remote Started Car")

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
