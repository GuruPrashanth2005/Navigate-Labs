a=int(input("n: "))
b=int(input("m: "))
while b:    
    a,b=b,a%b
print("GCD is:",a)
