l=float(input("litre(s):"))
p=float(input("price:"))
bill=int(l*p)
digit=bill%10

if digit<=4:
    bill=bill+digit
else:
    bill=bill+(10-digit)
print(bill)