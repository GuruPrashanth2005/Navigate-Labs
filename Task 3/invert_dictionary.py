import ast

user_input = input("Enter dictionary {student: dept}: ")
student_dept = ast.literal_eval(user_input)

dept_students = {}

for student, dept in student_dept.items():
    if dept not in dept_students:
        dept_students[dept] = []
    dept_students[dept].append(student)

print(dept_students)