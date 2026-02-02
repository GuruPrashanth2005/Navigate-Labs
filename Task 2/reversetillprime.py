n=int(input("n: "))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
for i in range (2,rev):
    if rev%i==0:
        prime=False
        break
if prime:
    print("PRIME")
else:
    print("NOT PRIME")