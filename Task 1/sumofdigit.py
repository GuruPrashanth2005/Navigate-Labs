n=int(input("n: "))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print("Sum of digits is:",sum)