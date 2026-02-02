d=int(input("d:"))
if 1<=d<=5:
    charge=d*2
elif 6<=d<=10:
    charge=d*3
else:
    charge=d*5
print(f"charge:{charge}")