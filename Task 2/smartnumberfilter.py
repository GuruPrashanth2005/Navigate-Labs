n=int(input("n: "))
sum=0
while n>0:
    if n%10 in [2,3,5,7]:
        sum+=n%10
    n=n//10
print(sum)