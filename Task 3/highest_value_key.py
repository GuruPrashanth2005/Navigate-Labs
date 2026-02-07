import ast

user_input = input("Enter a dictionary (e.g., {'a': 10, 'b': 50, 'c': 20}): ")
data = ast.literal_eval(user_input)

if data:
    max_key = max(data, key=data.get)
    print(f"Key with the highest value: {max_key}")
else:
    print("Dictionary is empty.")