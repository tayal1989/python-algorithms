class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Namaste")

def call_talk(obj):
    obj.talk()

d = Duck()
call_talk(d)

h = Human()
call_talk(h)

class Engine:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start()

class AirBusEngine:
    def start(self):
        print("Started airbus engine")

class BoeingEngine:
    def start(self):
        print("Started boeing engine")

ae = AirBusEngine()
e1 = Engine(ae)
e1.start_engine()

be = BoeingEngine()
e2 = Engine(be)
e2.start_engine()
