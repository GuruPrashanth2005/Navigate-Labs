import ast

user_input = input("Enter your dictionary (e.g., {'a': 1, 'b': 2}): ")
original_dict = ast.literal_eval(user_input)

reversed_dict = {value: key for key, value in original_dict.items()}

print(reversed_dict)