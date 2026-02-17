class Delivery:
    def deliver(self): pass

class Air(Delivery):
    def deliver(self): print("Air Delivery")

class Ground(Delivery):
    def deliver(self): print("Ground Delivery")

for d in [Air(), Ground()]:
    d.deliver()
