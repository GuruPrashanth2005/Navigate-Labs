class Device:
    def __init__(self, id):
        self.id = id
        self.status = False

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

d = Device("D1")
d.turn_on()
print("Status:", d.status)
