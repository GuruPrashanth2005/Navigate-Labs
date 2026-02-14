class Bill:
    def __init__(self, units):
        self.units = units

class Electricity(Bill):
    def amount(self):
        return self.units * 6

b = Electricity(100)
print("Bill:", b.amount())
