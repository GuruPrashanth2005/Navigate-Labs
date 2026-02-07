list1 = [int(x) for x in input("Enter first list: ").split()]
list2 = [int(x) for x in input("Enter second list: ").split()]
list3 = [int(x) for x in input("Enter third list: ").split()]

common = list(set(list1) & set(list2) & set(list3))

print(common)