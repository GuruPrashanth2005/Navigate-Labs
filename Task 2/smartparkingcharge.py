n=float(input("n:"))
if n<=2:
    charge=n*20
elif n<=5:
    charge=2*20+(n-2)*15
else:
    charge=2*20+3*15+(n-5)*10
print(f"charge:{charge}")
