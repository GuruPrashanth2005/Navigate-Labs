n=int(input("n: "))
product=1
while n>0:
    digit=n%10
    product*=digit
    n=n//10
print("Product of digits is:",product)