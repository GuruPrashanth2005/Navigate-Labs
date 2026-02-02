n=int(input("n: "))
sum=0
product=1
while n>0:
    digit=n%10
    sum+=digit
    product*=digit
    n=n//10
if sum%2==0 and product%3==0:
    print("VALID")
else:
    print("INVALID")