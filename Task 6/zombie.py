class Enemy:
    def act(self):
        pass


class Zombie(Enemy):
    def act(self):
        print("Zombie attacks slowly")


class Alien(Enemy):
    def act(self):
        print("Alien attacks with laser")


enemies = [Zombie(), Alien()]

for e in enemies:
    e.act()
