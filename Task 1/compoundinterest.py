p=float(input("P:"))
r=float(input("R:"))
t=float(input("T:"))
ci = p*(1+(r / 100))**t - p
print("compound interest: ", ci)