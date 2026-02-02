w=float(input("weight: "))
p=float(input("price: "))
bill=w*p
if w>10:
    bill *= 0.95
print(bill)