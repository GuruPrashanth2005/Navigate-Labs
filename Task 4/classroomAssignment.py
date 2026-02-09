submissions = eval(input("Submissions (student: [assignment_ids]): "))
all_assignments = set().union(*submissions.values()) if submissions else set()
submitted_all = [s for s, aids in submissions.items() if set(aids) == all_assignments]
not_submitted = set().union(*submissions.values()) if submissions else set()
print(f"Submitted all: {submitted_all if submitted_all else 'None'}")
print(f"Not submitted by anyone: {not_submitted}")