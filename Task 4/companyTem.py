n = int(input("Number of employees: "))
skills = {input(f"Employee {i+1}: "): set(input("Skills: ").split(", ")) for i in range(n)}
both = [e for e, s in skills.items() if {'Python', 'SQL'}.issubset(s)]
all_skills = set().union(*skills.values())
print(f"Python & SQL: {both}")
print(f"All skills: {all_skills}")