n=int(input("n: "))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
if sum%9==0:
    print("VALID")
else:
    print("INVALID")