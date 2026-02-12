n=input(("input:"))
if n.isalpha():
    print("Invalid")
elif n.isdigit():
    m=int(n)
    if 2<=m<=7 and m%2==0:
        print("WEIRD")
    elif 8<=m<=20 and m%2==0:
        print("NOT WEIRD")
    elif m%2!=0:
        print("INVALID")
    elif m>100:
        print("INVALID")


