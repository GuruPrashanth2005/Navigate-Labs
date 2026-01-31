balance=int(input("Enter your account balance: "))
withdrawal=int(input("Enter withdrawal amount: "))
if withdrawal%100==0:
    if withdrawal<=balance:
        balance-=withdrawal
        if balance>=500:
            print(f"Transaction successful. Remaining balance: {balance}")
        else:
            print(f"Transaction successful. Remaining balance: {balance}. Please maintain a minimum balance of 500.")
    else:
        print("Insufficient balance")
elif withdrawal>balance or withdrawal%100!=0:
    print("Error: Insufficient funds or invalid withdrawal amount must be multiple of 100")
