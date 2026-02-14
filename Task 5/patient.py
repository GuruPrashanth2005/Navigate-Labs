class Patient:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def cost(self):
        return 5000 if self.category == "General" else 10000

p = Patient("Raj", "Special")
print("Cost:", p.cost())
