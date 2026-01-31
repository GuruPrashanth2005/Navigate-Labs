a=int(input("a: "))
b=int(input("b: "))
x,y=a,b
while b:    
    a,b=b,a%b
lcm=(x*y)//a
print("LCM is:",lcm)