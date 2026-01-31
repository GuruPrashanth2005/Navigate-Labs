n=int(input("n: "))
count=0
while n>0:
    digit=n%10
    count+=1
    n=n//10
print("Number of digits is:",n)