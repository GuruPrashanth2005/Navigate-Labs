n=int(input("n:"))
isPrime=True 
for i in range(2,n):
    if n % i == 0:
        isPrime = False
        break
if isPrime:
    print("Prime number")
else:
    print("not prime")
    