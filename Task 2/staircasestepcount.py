n=int(input("stairs: "))
k=int(input("size: "))
steps=n//k
if n%k!=0:
    steps=steps+1
print(steps)