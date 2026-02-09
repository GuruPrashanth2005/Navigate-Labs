traffic = eval(input("Traffic data (nested list): "))
junction_totals = [sum(row) for row in traffic]
max_junction = junction_totals.index(max(junction_totals)) + 1
hourly_totals = [sum(traffic[i][h] for i in range(len(traffic))) for h in range(len(traffic[0]))]
max_hour = hourly_totals.index(max(hourly_totals)) + 1
print(f"Junction with highest traffic: Junction {max_junction}")
print(f"Hour with highest traffic: Hour {max_hour}")