lst = list(map(int, input().split()))
print("Sum of the list elements is:", sum(lst))
prod = 1
for i in lst:
    prod *= i
print("Product of the list elements is:", prod)
even, odd = 0, 0
for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("Number of even elements:", even)
print("Number of odd elements:", odd)
lar = -1
sec = -1
for i in lst:
    if i > lar:
        sec = lar
        lar = i
    elif i > sec and i != lar:
        sec = i
print("Second largest element is:", sec)
ind = int(input("Enter the index: "))
try:
    print(f"Element at index {ind} is:", lst[ind])
except IndexError:
    print("Index out of range")