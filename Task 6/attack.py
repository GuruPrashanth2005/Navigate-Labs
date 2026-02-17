class Character:
    def attack(self): pass

class Warrior(Character):
    def attack(self): print("Sword Attack")

class Archer(Character):
    def attack(self): print("Arrow Attack")

for c in [Warrior(), Archer()]:
    c.attack()
