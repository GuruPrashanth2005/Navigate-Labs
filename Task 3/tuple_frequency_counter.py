import ast

user_input = input("Enter list of tuples: ")
tuple_list = ast.literal_eval(user_input)

counts = {}

for item in tuple_list:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print(counts)