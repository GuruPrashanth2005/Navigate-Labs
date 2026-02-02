l=int(input("l:"))
w=int(input("w:"))
h=int(input("h:"))
total=l+w+h
if l<0 or w<0 or h<0:
    print("INVALID")
elif total<=150:
    print("ACCEPTED")
else:
    print("REJECTED")