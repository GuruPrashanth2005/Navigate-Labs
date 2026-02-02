n=int(input("n: "))
count=0
i=1
while i<=n:
    if '4' not in str(i):
        count=count+1
    i=i+1
print(count)