n=int(input("Enter a number: "))
if n<=0:
    print("invalid input")
elif n%5==0 and n%11==0:
    print(f"{n} is divisible by both 5 and 11")
elif n%5==0:
    print(f"{n} is divisible by 5")
elif n%11==0:
    print(f"{n} is divisible by 11")
else:
    print(f"{n} is not divisible by 5 or 11")