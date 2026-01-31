# import math
ask=input("enter R if rectangle or C if circle:").lower()
if ask=='r':
    l=float(input("enter length:"))
    b=float(input("enter breadth:"))
    area=l*b
    perimeter=2*(l+b)
    print("perimeter of rectangle:",perimeter)
    print("area of rectangle:",area)
elif ask=='c':
    r=float(input("enter radius:"))
    area=3.14*r*r
    circumference=2*3.14*r
    print("circumference of circle:",circumference)
    print("area of circle:",area)
else:
    print("invalid input")