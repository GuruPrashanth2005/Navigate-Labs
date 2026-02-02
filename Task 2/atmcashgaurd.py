b=int(input("b: "))
w=int(input("w: "))
remining=b-w
if w%100==0:
    if w<=b:
        if remining>=500:
            print("SUCCESS")
        else:
            print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")
    