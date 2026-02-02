n=input("n: ")
i=0
while i<len(n):
    if n[i]=='0':
        haszero=True
        break
    else:
        haszero=False
    i+=1   
if haszero and n[-1]=='5':
    print("OPEN")
else:
    print("LOCKED")