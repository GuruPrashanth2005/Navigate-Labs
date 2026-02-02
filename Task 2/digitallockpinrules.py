n=int(input("n:"))
sum=0
count=0
while n>0:
    digit=n%10
    count+=1
    sum+=digit
    n=n//10
if  digit==4 and sum>=15:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")