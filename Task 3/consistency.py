import ast

user_input = input("Enter list of dictionaries: ")
records = ast.literal_eval(user_input)

if not records:
    print("List is empty.")
else:
    first_keys = set(records[0].keys())
    consistent = all(set(record.keys()) == first_keys for record in records)
    
    if consistent:
        print("Consistent")
    else:
        print("Inconsistent")