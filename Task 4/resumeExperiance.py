experience = eval(input("Experience data (candidate: [years]): "))
total_exp = {c: sum(years) for c, years in experience.items()}
avg_exp = sum(total_exp.values()) / len(total_exp) if total_exp else 0
above_avg = [c for c, exp in total_exp.items() if exp > avg_exp]
print(f"Total experience: {total_exp}")
print(f"Above average: {above_avg if above_avg else 'None'}")