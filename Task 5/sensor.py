class Sensor:
    def read(self):
        return 25

s = Sensor()
print("Temperature:", s.read())
