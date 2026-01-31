n=int(input("n: "))
number=n
count=0
while n>0:
    digit=n%10
    count=count*10+digit
    n=n//10 
if count==number:
    print("Palindrome")
else:
    print("Not a palindrome")
