B=int(input("Enter battery: "))
D=int(input("Enter drop per hour: "))
if B<20:
    print(0)
else:
    hours=0
    while B>=20:
        B-=D
        hours+=1
    print(hours)