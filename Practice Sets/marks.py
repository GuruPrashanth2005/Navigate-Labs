# def gradesum():
#     a=int(input("a:"))
#     b=int(input("b:"))
#     c=int(input("c:"))
#     d=int(input("d:"))
#     e=int(input("e:"))
#     sum=a+b+c+d+e
#     avg=sum/5
#     if a<35 or b<35 or c<35 or d<35 or e<35:
#         return "Fail"
#     else:
#         return "Pass",avg,"Total:",sum

# print(gradesum())

# password=input("password:")
# def passw():
#     length = len(password)
#     if length>=8:
#         for i in range (length):
#             if (password[i].isupper()) and  (password[i].islower()) and (password[i].isdigit()):
#                 upper=True
#             else:
#                 upper=False
#         if upper:
#             print("valid")
#         else:
#             print("invalid")
#     else:
#         print("Use 8 characters")
# passw()
# def deposit(amount):
#     amt = float(input("Enter amount to deposit: "))
#     return amount + amt
# def withdraw(amount):
#     amt = float(input("Enter amount to withdraw: "))
#     if amt > amount:
#         print("Insufficient balance")
#         return amount
#     else:
#         amount -= amt
#         if amount < 500:
#             print("Balance below minimum required balance of 500")
#         return amount
# def check_balance(amount):
#     return amount
# amount = int(input("Enter initial amount in your bank account: "))
# while True:
#     print("1. Deposit")
#     print("2. Withdraw")
#     print("3. Check Balance")
#     print("4. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         amount = deposit(amount)
#         print(f"New balance: {amount}")
#     elif choice == 2:
#         amount = withdraw(amount)
#         print(f"New balance: {amount}")
#     elif choice == 3:
#         print(f"Current balance: {check_balance(amount)}")
#     elif choice == 4:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice, please try again.")

def rangeprime(start, end):
    res = []
    for num in range(start, end + 1):
        for i in range(2,int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            res.append(num)
    return res
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Prime numbers in the range are:", rangeprime(start, end))
    