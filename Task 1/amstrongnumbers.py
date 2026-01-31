n=int(input("n: "))
number=n
count=0
digit=0
sum=0
while n>0:
    digit=n%10
    count+=1
    n=n//10
while number>0:
    digit=number%10
    sum+=digit**count
    number=number//10
if number==n:
    print("Armstrong number")   
else:
    print("Not an Armstrong number")