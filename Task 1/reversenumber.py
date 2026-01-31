n=int(input("n: "))
count=0
while n>0:
    digit=n%10
    count=count*10+digit
    n=n//10
print("Reversed number is:",count)