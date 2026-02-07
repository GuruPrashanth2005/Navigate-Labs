import ast

user_input = input("Enter list of tuples (e.g., [(1,2), (2,1), (3,4)]): ")
pairs = ast.literal_eval(user_input)

seen = set()
result = []

for a, b in pairs:
    canonical = tuple(sorted((a, b)))
    if canonical not in seen:
        seen.add(canonical)
        result.append((a, b))

print(result)