enrollments = eval(input("Enrollments (course: set([students])): "))
all_students = set().union(*enrollments.values()) if enrollments else set()
multi_enrolled = [s for s in all_students if sum(1 for course in enrollments.values() if s in course) > 1]
max_course = max(enrollments, key=lambda c: len(enrollments[c]))
print(f"Multi-course students: {multi_enrolled if multi_enrolled else 'None'}")
print(f"Max enrollment: {max_course} ({len(enrollments[max_course])} students)")