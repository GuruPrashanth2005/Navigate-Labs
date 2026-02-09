orders = eval(input("Orders (list): "))
order_count = {}
for o in orders:
    order_count[o] = order_count.get(o, 0) + 1
most_ordered = max(order_count, key=order_count.get)
ordered_once = [o for o, c in order_count.items() if c == 1]
print(f"Most ordered: {most_ordered}")
print(f"Ordered once: {ordered_once}")