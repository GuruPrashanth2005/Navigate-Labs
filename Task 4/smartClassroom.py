usage = eval(input("Device usage (device_id: [hours]): "))
total_usage = {d: sum(h) for d, h in usage.items()}
avg_all = sum(total_usage.values()) / len(total_usage) if total_usage else 0
above_avg = [d for d, t in total_usage.items() if t > avg_all]
print(f"Total usage: {total_usage}")
print(f"Above average: {above_avg if above_avg else 'None'}")