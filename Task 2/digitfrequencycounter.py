n=int(input("number: "))
d=int(input("digit: "))
count=0
while n>0:
    if n%10==d:
        count+=1
    n//=10
print(count)