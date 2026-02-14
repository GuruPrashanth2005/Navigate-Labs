class Character:
    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print("Sword Attack")

w = Warrior()
w.attack()
