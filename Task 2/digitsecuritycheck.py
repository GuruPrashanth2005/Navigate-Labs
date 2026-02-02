n=int(input("n: "))
sum=0
last=n%10
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
if sum%3==0:
    if last%2==0:
        print("VALID")
    else:
        print("INVALID")
else:
    print("INVALID")
