a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))  
if a+b>c and b+c>a and c+a>b:
    if a==b==c:
        print("Equilateral triangle")
    elif a==b or b==c or c==a:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")