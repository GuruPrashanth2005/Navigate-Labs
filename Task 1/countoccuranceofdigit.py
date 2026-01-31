n = int(input("n: "))
d = int(input("d: "))
count = 0
if n == 0 and d == 0:
    count = 1
else:
    while n > 0:
        digit = n % 10
        if digit == d:
            count += 1
        n //= 10
print("Count of digit", d, "is:", count)
