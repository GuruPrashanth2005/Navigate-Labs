n=int(input("n: "))
copy=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if copy==rev:
    print("YES")
else:
    print("NO")

