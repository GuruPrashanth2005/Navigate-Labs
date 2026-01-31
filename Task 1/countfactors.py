n=int(input("n: "))
count=0
for i in range(1,n):
    if n%i==0:
        print(i,end=" ")
        count+=1
print("\nNumber of factors:",count)