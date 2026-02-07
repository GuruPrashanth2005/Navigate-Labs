import ast

user_input = input("Enter student dictionary (e.g., {'Name': [m1, m2]}): ")
student_data = ast.literal_eval(user_input)

averages = {name: sum(marks) / len(marks) for name, marks in student_data.items() if marks}

print(averages)