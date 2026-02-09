scores = eval(input("Quiz scores (student: [scores]): "))
avg_per_student = {s: sum(sc) / len(sc) for s, sc in scores.items()}
class_avg = sum(avg_per_student.values()) / len(avg_per_student)
above_avg = [s for s, a in avg_per_student.items() if a > class_avg]
print(f"Averages: {avg_per_student}")
print(f"Above class avg: {above_avg}")