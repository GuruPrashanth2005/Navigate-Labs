import ast

user_input = input("Enter list of student records: ")
students = ast.literal_eval(user_input)

top_students = {}

for student in students:
    dept = student["dept"]
    score = student["score"]
    
    if dept not in top_students or score > top_students[dept]["score"]:
        top_students[dept] = student

print(top_students)