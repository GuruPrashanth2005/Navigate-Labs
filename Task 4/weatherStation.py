temps = eval(input("Weekly temps (nested list): "))
avg_per_week = [sum(week) / len(week) for week in temps]
hottest = max(sum(temps, []))
week_max = avg_per_week.index(max(avg_per_week)) + 1
print(f"Avg per week: {avg_per_week}")
print(f"Hottest: {hottest}")
print(f"Week with highest avg: {week_max}")