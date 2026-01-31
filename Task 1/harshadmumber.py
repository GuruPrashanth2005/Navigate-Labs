n=int(input("n: "))
sum=0
copy=n
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
    if sum==1:
        break
if copy%sum==0:
    print("Harshad number") 
else:
    print("Not a Harshad number")
    
