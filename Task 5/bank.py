class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid withdrawal")

    def display(self):
        print("Balance:", self.balance)

acc = BankAccount("102", "Suriya", 5000)
acc.deposit(500)
acc.withdraw(200)
acc.display()
