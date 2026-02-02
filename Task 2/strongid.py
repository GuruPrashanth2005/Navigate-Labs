n=int(input("n: "))
product=1
copy=n
sum=0
while n>0:
    digit=n%10
    product=1
    for i in range(1,digit+1):
        product*=i
    sum+=product
    n=n//10
if sum==copy:
    print("STRONG")
else:   
    print("NOT STRONG")