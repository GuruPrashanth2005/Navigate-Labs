inventory = eval(input("Inventory (list of dicts): "))
zero_stock = [i['product_id'] for i in inventory if i['stock'] <= 0]
out_of_stock_cats = set()
for i in inventory:
    if i['stock'] <= 0:
        out_of_stock_cats.add(i['category'])
all_positive = all(i['stock'] > 0 for i in inventory)
print(f"Zero stock: {zero_stock if zero_stock else 'None'}")
print(f"All positive: {all_positive}")
print(f"Categories with out-of-stock: {out_of_stock_cats if out_of_stock_cats else 'None'}")