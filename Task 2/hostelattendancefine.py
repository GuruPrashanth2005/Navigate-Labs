percentage=int(input("p: "))
if percentage<75:
    fine=(75-percentage)*10
else:
    fine=0
print(f"fine:{fine}")