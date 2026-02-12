nums=list(map(int, input().split()))
k=int(input())
count=0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j]==k:
            count+=1
print(count)
