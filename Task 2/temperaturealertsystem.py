n=int(input("n: "))
for i in range(n):
    t=int(input("temperature: 1"))
    if t>45:
        print("ALERT")
        break
else:
    print("SAFE")