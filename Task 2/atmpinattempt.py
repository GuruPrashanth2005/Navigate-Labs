pin=int(input("Enter correct PIN: "))
for i in range(3):
    entry=int(input("attempt: "))
    if entry==pin:
        print("ACCESS GRANTED")
        break
else:
    print("CARD BLOCKED")