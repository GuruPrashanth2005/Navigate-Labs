import ast

config_input = input("Enter configuration dictionary: ")
required_input = input("Enter set of required keys: ")

config = ast.literal_eval(config_input)
required_keys = ast.literal_eval(required_input)

current_keys = set(config.keys())

missing_keys = required_keys - current_keys
extra_keys = current_keys - required_keys

print(f"Missing keys: {missing_keys}")
print(f"Extra keys: {extra_keys}")