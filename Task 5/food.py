class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Veg(Food):
    def final_price(self):
        return self.price

f = Veg("Dosa", 50)
print("Bill:", f.final_price())
