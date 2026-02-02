n=int(input("n: "))
minimum=float(input("minimum: "))
for i in range(n+1-1):
    time=float(input("time: "))
    if time<minimum:
        minimum=time
print(f"Fastest Time: {minimum}(s)")

   