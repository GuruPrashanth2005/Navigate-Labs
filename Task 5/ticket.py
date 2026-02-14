class Ticket:
    def __init__(self, source, dest, distance):
        self.source = source
        self.dest = dest
        self.distance = distance

class Bus(Ticket):
    def fare(self):
        return self.distance * 5

t = Bus("A", "B", 10)
print("Fare:", t.fare())
