a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=a+b
d=a*b
if c>d:
    print(f"sum {c}")
    print("Sum is greater than Product")
elif d>c:   
    print(f"Product {d}")
    print("Product is greater than Sum")   
else:
    print("Sum and Product are equal")