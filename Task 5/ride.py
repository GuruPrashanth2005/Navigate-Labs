class Ride:
    def __init__(self, distance):
        self.distance = distance

class Premium(Ride):
    def fare(self):
        return self.distance * 15

r = Premium(10)
print("Fare:", r.fare())
