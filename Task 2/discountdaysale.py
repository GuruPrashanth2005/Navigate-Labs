n=int(input("n: "))
if n<1000:
    discount=0
elif 1000<=n<=2999:
    discount=n*0.10
elif 3000<=n<=4999:
    discount=n*0.20
else:
    discount=n*0.30
final_price=n-discount
print(f"Discount: {discount}")
print(f"Final Price: {final_price}")