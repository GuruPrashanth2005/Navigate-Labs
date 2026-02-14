class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "via Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "via UPI")

p = UPI()
p.pay(1500)
