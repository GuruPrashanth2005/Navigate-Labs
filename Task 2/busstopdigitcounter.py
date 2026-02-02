n=int(input("n: "))
odd_count=0
even_count=0
while n>0:
    digit=n%10
    if digit%2==0:
        even_count+=1
    else:
        odd_count+=1
    n=n//10
print(f"Odd Count: {odd_count}")
print(f"Even Count: {even_count}")