customers = eval(input("Purchases (customer: amount): "))
final = {}
for c, amt in customers.items():
    discount = 0.2 if amt > 10000 else 0.1 if amt > 5000 else 0
    final[c] = amt * (1 - discount)
print(f"Final amounts: {final}")