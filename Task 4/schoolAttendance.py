n = int(input("Number of students: "))
attendance = {input(f"Student {i+1}: "): set(input("Days present: ").split(", ")) for i in range(n)}
total_days = {s: len(days) for s, days in attendance.items()}
all_days = set().intersection(*attendance.values()) if attendance else set()
print(f"Total days: {total_days}")
print(f"Attended all days: {[s for s in attendance if len(attendance[s]) == len(all_days)]}")