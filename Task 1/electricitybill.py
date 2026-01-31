unit=int(input("Enter units consumed: "))
if unit<=100:
    bill=unit*1.50
elif unit<=200:
    bill=100*1.50+(unit-100)*2.50
elif unit<=300:
    bill=100*1.50+100*2.50+(unit-200)*4.00
else:
    bill=100*1.50+100*2.50+100*4.00+(unit-300)*6.00
print("bill amount is:",bill)