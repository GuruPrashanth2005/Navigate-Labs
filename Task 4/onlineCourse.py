progress = eval(input("Course progress (student: set([lessons])): "))
all_lessons = set().union(*progress.values()) if progress else set()
completed_all = [s for s, lessons in progress.items() if lessons == all_lessons]
less_than_half = [s for s, lessons in progress.items() if len(lessons) < len(all_lessons) / 2]
print(f"Completed all: {completed_all if completed_all else 'None'}")
print(f"Less than half: {less_than_half if less_than_half else 'None'}")