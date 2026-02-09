students = eval(input("Student records (list of dicts): "))
dept_cgpa = {}
for s in students:
    if s['dept'] not in dept_cgpa:
        dept_cgpa[s['dept']] = []
    dept_cgpa[s['dept']].append(s['cgpa'])
summary = {d: sum(c) / len(c) for d, c in dept_cgpa.items()}
print(f"Department averages: {summary}")