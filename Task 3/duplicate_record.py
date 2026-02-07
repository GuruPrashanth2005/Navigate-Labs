import ast

user_input = input("Enter list of dictionaries: ")
records = ast.literal_eval(user_input)

seen = []
duplicates = []

for record in records:
    if record in seen:
        if record not in duplicates:
            duplicates.append(record)
    else:
        seen.append(record)

print(f"Duplicate records: {duplicates}")