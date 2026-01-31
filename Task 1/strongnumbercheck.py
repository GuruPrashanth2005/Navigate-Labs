n=int(input("n: "))
sum=0
copy=n
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    n=n//10
if sum==copy:
    print("Strong number")
else:
    print("Not a strong number")