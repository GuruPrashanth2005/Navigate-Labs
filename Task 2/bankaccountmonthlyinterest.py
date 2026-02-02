balance=int(input("b: "))
if balance<10000:
    interest=0.03
elif 10000<=balance<=50000:
    interest=0.05
else:
    interest=0.07
monthly=(balance*interest)/12
print(f"monthly interest:{monthly}")