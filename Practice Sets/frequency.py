n=list(map(int,input().split()))
result=[]
for i in n:
    count=0
    for j in n:
        if i==j:
            count+=1
    if count==1:
        result.append(i)
print(result)