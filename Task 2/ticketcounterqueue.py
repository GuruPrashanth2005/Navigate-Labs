age=int(input("age: "))
price=200
if age<5:
    price=0
elif age>=5 and age<13:
    discount=price*0.50
    price=price-discount
elif age>=13 and age<60:
    price=price
elif age>=60:
    discount=price*0.30
    price=price-discount
print(f"Ticket Price: {price}")
