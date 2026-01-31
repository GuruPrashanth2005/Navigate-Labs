n = int(input("n: "))
largest = -1
second_largest = -1
while n > 0:
    digit = n % 10
    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit < largest and digit > second_largest:
        second_largest = digit
    n //= 10
print("Second largest digit:", second_largest)