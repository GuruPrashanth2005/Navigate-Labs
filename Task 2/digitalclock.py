h=int(input("hour(s):"))
m=int(input("minute(s):"))
x=int(input("extra:"))
m=m+x
h=h+(m//60)
m=m%60
h=h%24
print(f"{h} hour(s):{m} minute(s)")
