import ast

required_input = input("Enter required skills with weights (e.g., {'python': 5, 'sql': 3}): ")
candidate_input = input("Enter candidate skills with proficiency (e.g., {'python': 4, 'sql': 2, 'java': 5}): ")

required_skills = ast.literal_eval(required_input)
candidate_skills = ast.literal_eval(candidate_input)

total_score = sum(
    weight * candidate_skills[skill] 
    for skill, weight in required_skills.items() 
    if skill in candidate_skills
)

print(f"Match Score: {total_score}")