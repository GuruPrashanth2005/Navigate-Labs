class Package:
    def __init__(self, status):
        self.status = status

p = Package("Shipped")
print("Status:", p.status)
