students = {}
n = int(input("Number of students: "))
for i in range(n):
    name = input(f"Student {i+1} name: ")
    modules = input(f"Modules for {name}: ").split(", ")
    students[name] = modules
counts = {s: len(m) for s, m in students.items()}
topper = max(counts, key=counts.get)
print(f"Counts: {counts}")
print(f"Max: {topper} ({counts[topper]})")