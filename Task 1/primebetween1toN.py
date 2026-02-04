n=int(input("n: "))
count=0
for i in range(1,n+1):
    isPrime=True
    for j in range(2,i):
        if i%j==0:
            isPrime=False
            break
    if isPrime:
        print(i,end=" ")