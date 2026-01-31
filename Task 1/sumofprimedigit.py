n=int(input("n: "))
sum=0
while n>0:
    digit=n%10
    if digit==2 or digit==3 or digit==5 or digit==7:
        sum+=digit
    n=n//10
print("Sum:",sum)