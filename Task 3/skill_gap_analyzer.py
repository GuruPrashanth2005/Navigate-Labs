required_input = input("Enter required skills (comma-separated): ")
student_input = input("Enter student skills (comma-separated): ")

required_skills = {s.strip().lower() for s in required_input.split(',')}
student_skills = {s.strip().lower() for s in student_input.split(',')}

missing_skills = required_skills - student_skills
extra_skills = student_skills - required_skills

print(f"\nMissing Skills: {missing_skills if missing_skills else 'None'}")
print(f"Extra Skills: {extra_skills if extra_skills else 'None'}")