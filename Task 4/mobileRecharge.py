usage = eval(input("Usage data (user_id: [daily_usage]): "))
limit = int(input("Usage limit: "))
exceeded = [u for u, vals in usage.items() if sum(vals) > limit]
avg_usage = {u: sum(vals) / len(vals) for u, vals in usage.items()}
max_user = max(avg_usage, key=avg_usage.get) if avg_usage else None
print(f"Exceeded limit: {exceeded if exceeded else 'None'}")
print(f"Highest avg: {max_user} ({avg_usage[max_user]:.2f})")