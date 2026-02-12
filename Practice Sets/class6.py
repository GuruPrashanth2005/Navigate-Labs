class Employee:
    def deposite(self):
        deposite = int(input("Deposite amount: "))
        self.__deposite=deposite
    def withdraw(self):
        withdraw = int(input("Withdraw amount: "))
        self.__withdraw=withdraw
    def balance(self):
        amount = self.__deposite - self.__withdraw
        print("Balance:",amount)
account = Employee()
print("Welcome to the Bank")
account.deposite()
account.withdraw()
account.balance()

