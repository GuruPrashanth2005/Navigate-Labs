n=int(input("n:"))
count=0
for i in range(2,n*2+1,2):
    count+=i
    print(i,end=" ")
print("Sum of even numbers is:",count)
