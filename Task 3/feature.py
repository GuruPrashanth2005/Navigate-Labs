import ast

user_input = input("Enter dictionary {feature: importance}: ")
data = ast.literal_eval(user_input)

total_sum = sum(data.values())

normalized_data = {key: value / total_sum for key, value in data.items()}

print(f"Normalized Dictionary: {normalized_data}")
print(f"Total Sum: {sum(normalized_data.values())}")