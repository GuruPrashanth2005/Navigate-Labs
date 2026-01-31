a=int(input("Enter coefficient a: "))
b=int(input("Enter coefficient b: "))
c=int(input("Enter coefficient c: "))
d=(b**2-4*a*c)**0.5
if d>0:
    root1=(-b + d)/(2*a)
    root2=(-b - d)/(2*a)
    print(f"Roots are real and different: {root1} and {root2}")
elif d==0:
    root=-b/(2*a)
    print(f"Root is real and same: {root}")
else:
    print("Roots are complex")