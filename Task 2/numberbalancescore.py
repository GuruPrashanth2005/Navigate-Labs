n=int(input("n: "))
s=str(n)
length=len(s)
half_length=length//2
left_sum=0
right_sum=0
for i in range(half_length):
        left_sum += int(s[i])
        right_sum += int(s[i + half_length])
if left_sum == right_sum:
        print("Balanced")
        print(f"left:{left_sum},right:{right_sum}")
else:
        print("Not Balanced")
