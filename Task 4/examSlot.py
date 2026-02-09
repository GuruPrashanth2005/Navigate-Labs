assignments = []
n = int(input("Number of assignments: "))
for _ in range(n):
    student, slot = input("Enter (student, slot): ").split(", ")
    assignments.append((student, int(slot)))
students = [s for s, _ in assignments]
slots = [sl for _, sl in assignments]
dup_students = [s for s in set(students) if students.count(s) > 1]
dup_slots = [sl for sl in set(slots) if slots.count(sl) > 1]
print(f"\nDuplicate students: {dup_students if dup_students else 'None'}")
print(f"Duplicate slots: {dup_slots if dup_slots else 'None'}")
print(f"Valid: {not dup_students and not dup_slots}")
