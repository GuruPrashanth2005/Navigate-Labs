import ast

user_input = input("Enter list of tuples (name, score): ")
data = ast.literal_eval(user_input)

data.sort(key=lambda x: x[1], reverse=True)

print("Sorted scores:")
for name, score in data:
    print(f"{name}: {score}")