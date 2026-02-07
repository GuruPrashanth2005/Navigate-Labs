import ast

user_input = input("Enter list of dictionaries (dataset rows): ")
data = ast.literal_eval(user_input)

summary = {
    "rows": len(data),
    "unique_values": {}
}

if data:
    keys = data[0].keys()
    for key in keys:
        unique_count = len({row[key] for row in data})
        summary["unique_values"][key] = unique_count

print(summary)