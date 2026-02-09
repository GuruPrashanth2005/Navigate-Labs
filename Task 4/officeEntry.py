logs = eval(input("Entry logs (list of tuples): "))
entry_times = {}
invalid = []
for emp, time in logs:
    if (emp, time) in entry_times.values() if entry_times else False:
        invalid.append((emp, time))
    entry_times[(emp, time)] = True
time_entries = {}
for emp, time in logs:
    if time not in time_entries:
        time_entries[time] = []
    time_entries[time].append(emp)
invalid = [(emp, t) for t, emps in time_entries.items() for emp in emps if time_entries[t].count(emp) > 1]
print(f"Invalid entries: {invalid if invalid else 'None'}")