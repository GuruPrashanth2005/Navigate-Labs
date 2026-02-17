class Vehicle:
    def start(self): pass
    def stop(self): pass

class Car(Vehicle):
    def start(self): print("Car started")
    def stop(self): print("Car stopped")

class Bike(Vehicle):
    def start(self): print("Bike started")
    def stop(self): print("Bike stopped")

for v in [Car(), Bike()]:
    v.start()
    v.stop()
