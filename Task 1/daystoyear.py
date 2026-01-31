days=int(input("Enter total days: "))
weeks = days // 7
remaining_days = days % 7
years = weeks // 52
remaining_weeks = weeks % 52
print(f"{years} year(s), {remaining_weeks} week(s), and {remaining_days} day(s)")
