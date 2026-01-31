cost=float(input("Enter cost price: "))
selling=float(input("Enter selling price: "))
profit=selling - cost
if profit>0:
    print(f"Profit is: {profit}")
elif profit<0:
    print(f"Loss is: {-profit}")
else:   
    print("No profit no loss")
