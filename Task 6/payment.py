from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount): pass
class Card(Payment):
    def pay(self, amount):
        print("Paid by Card:", amount)
class UPI(Payment):
    def pay(self, amount):
        print("Paid by UPI:", amount)
def checkout(method):
    method.pay(1000)
checkout(Card())
checkout(UPI())