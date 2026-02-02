late = int(input("late: "))
if late<=10:
    penalty=0
elif late<=30:
    penalty=50
else:
    penalty=100
print(penalty)
