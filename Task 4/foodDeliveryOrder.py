# Food Delivery Order Consistency
orders = eval(input("Orders (list of dicts): "))
no_items = [o['order_id'] for o in orders if not o.get('items') or len(o['items']) == 0]
dup_items = {}
for o in orders:
    items_count = {}
    for item in o.get('items', []):
        items_count[item] = items_count.get(item, 0) + 1
    if any(c > 1 for c in items_count.values()):
        dup_items[o['restaurant']] = [i for i, c in items_count.items() if c > 1]
print(f"No items: {no_items if no_items else 'None'}")
print(f"Duplicate items: {dup_items if dup_items else 'None'}")
