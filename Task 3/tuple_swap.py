user_input = input("Enter two elements separated by a space: ")
tup = tuple(user_input.split())

tup = (tup[1], tup[0])

print(tup)