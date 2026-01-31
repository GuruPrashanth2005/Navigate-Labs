n=int(input("n: "))
evencount=0
oddcount=0
for i in range(1,n+1):
    if i%2==0:
        evencount+=1
    else:
        oddcount+=1
print("Number of even numbers is:",evencount)
print("Number of odd numbers is:",oddcount)