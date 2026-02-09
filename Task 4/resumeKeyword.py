required = set(input("Required skills: ").split(", "))
n = int(input("Number of resumes: "))
for i in range(n):
    resume = set(input(f"Resume {i+1}: ").split(", "))
    match_pct = len(resume & required) / len(required) * 100
    missing = required - resume
    print(f"Resume {i+1}: {match_pct:.0f}% match, Missing: {missing if missing else 'None'}")