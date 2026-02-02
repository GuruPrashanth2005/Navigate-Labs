n=int(input("n: "))
count=0
while n>0:
    if n%10 in [2,3,5,7]:
        count+=1
    n=n//10
print(count)