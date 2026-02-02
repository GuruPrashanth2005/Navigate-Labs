a=int(input("a: "))
notes = [500,200,100,50,20,10,1]
count=0
for note in notes:
    count+=a//note
    a=a%note
print(count)

