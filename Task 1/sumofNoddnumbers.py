n=int(input("n:"))
sum=0
for i in range(1,n*2+1,2):
    sum+=i
    print(i,end=" ")
print("Sum of odd numbers is:",sum)