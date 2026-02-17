class Vehicle:
    def start(self): pass

class Bus(Vehicle):
    def start(self): print("Bus Engine Started")

class Car(Vehicle):
    def start(self): print("Car Engine Started")

for v in [Bus(), Car()]:
    v.start()
