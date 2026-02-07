list1 = [int(x) for x in input("Enter first list: ").split()]
list2 = [int(x) for x in input("Enter second list: ").split()]

result = list(set(list1) ^ set(list2))

print(result)