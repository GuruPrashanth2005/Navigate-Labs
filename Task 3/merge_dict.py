import ast

dict1_input = input("Enter first dictionary (e.g., {'a': 2, 'b': 3}): ")
dict2_input = input("Enter second dictionary (e.g., {'a': 4, 'b': 1}): ")

dict1 = ast.literal_eval(dict1_input)
dict2 = ast.literal_eval(dict2_input)

merged_dict = {key: dict1[key] + dict2.get(key, 0) for key in dict1}

print(merged_dict)