D =int(input("distance: "))
fare=0
if D>15:
    fare+=(D - 15)*6
    D=15
if D>5:
    fare+=(D - 5)*8
    D=5
fare +=D*10
print(fare)