n = int(input("n: "))
for d in range(10):
    temp=n 
    found=False
    while temp>0:
        digit=temp % 10
        if digit==d:
            found=True
            break
        temp=temp//10
    if not found:
            print(d)
            break
