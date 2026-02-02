S = int(input("seats: "))
N = int(input("bookings: "))
for i in range(N):
    if S>0:
        print("BOOKED")
        S-=1
    else:
        print("HOUSEFULL")
        break
if S>=0:
    print("Remaining seats:", S)