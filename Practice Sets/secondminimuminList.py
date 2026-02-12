# n=list(map(int,input("enter numbers:").split()))
# def sec_min(n):
#     min1=float('inf')
#     min2=float('inf')
#     for i in n:
#         if i<min1:
#             min2=min1
#             min1=i
#         elif i<min2 and i!=min1:
#             min2=i
#     if min2==float('inf'):
#         return None
#     return min2
# result=sec_min(n)
# if result is None:
#     print("no second value")
# else:
#     print(f"second value:{result}")

n=int(input("enter no of elements:"))
lst=[]
min1=float('inf')
min2=float('inf')
for i in range (n):
    lst.append(int(input()))
for i in lst:
    if i<min1:
        min2=min1
        min1=i
    elif i<min2 and i!=min1:
        min2=i
print(f"minimum element:{min2}")
