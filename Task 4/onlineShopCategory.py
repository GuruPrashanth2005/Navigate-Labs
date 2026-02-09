sales = eval(input("Sales (category: [amounts]): "))
total_per_cat = {c: sum(amounts) for c, amounts in sales.items()}
max_cat = max(total_per_cat, key=total_per_cat.get)
print(f"Total per category: {total_per_cat}")
print(f"Highest revenue: {max_cat} ({total_per_cat[max_cat]})")