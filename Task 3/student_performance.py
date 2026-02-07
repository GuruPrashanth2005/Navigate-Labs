import ast

user_input = input("Enter list of student dictionaries: ")
students = ast.literal_eval(user_input)

performance_map = {}

for student in students:
    name = student["name"]
    marks = student["marks"]
    attendance = student["attendance"]
    
    index = marks * 0.7 + attendance * 0.3
    performance_map[name] = index

topper = max(performance_map, key=performance_map.get)

print(f"Performance Indices: {performance_map}")
print(f"Topper: {topper}")