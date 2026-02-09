earnings = eval(input("Earnings (list of tuples): "))
total_earning = {}
delivery_count = {}
for pid, earning in earnings:
    total_earning[pid] = total_earning.get(pid, 0) + earning
    delivery_count[pid] = delivery_count.get(pid, 0) + 1
avg_per_delivery = {p: total_earning[p] / delivery_count[p] for p in total_earning}
max_avg = max(avg_per_delivery, key=avg_per_delivery.get)
print(f"Total earning: {total_earning}")
print(f"Partner with highest avg: {max_avg} ({avg_per_delivery[max_avg]:.2f})")