cart1 = eval(input("Cart 1 (dict): "))
cart2 = eval(input("Cart 2 (dict): "))
merged = {item: cart1.get(item, 0) + cart2.get(item, 0) for item in set(list(cart1.keys()) + list(cart2.keys()))}
print(f"Merged cart: {merged}")