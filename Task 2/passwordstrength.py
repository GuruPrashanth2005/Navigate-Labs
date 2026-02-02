n=int(input("password: "))
temp=n
count=0
has7=False
while temp>0:
    if temp%10==7:
        has7=True
    count+=1
    temp//=10
if has7 and count>=6:
    print("STRONG")
else:
    print("WEAK")