# marks=[
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ]
# for i in range (len(marks)):
#     total=0
#     for j in range (len(marks[i])):
#         total+=marks[i][j]
#         print(i+1)
# n = int(input("Enter number: "))
# lst = [x for x in range(1, n+1) if x % 3 == 0]
# print("List of numbers divisible by 3:", lst)

# n = int(input("Enter number: "))
# lst = [x for x in range(1, n+1) if x % 3 == 0]
# print("List of numbers divisible by 3:", lst)
# n = int(input("Enter number: "))
# lst = []
# for i in range(n):
#     name = input("Enter name: ")
#     marks = int(input("Enter marks: "))
#     lst.append((name, marks))
# lst.sort(key=lambda x: x[1], reverse=True)
# print(lst[0])


# n = int(input("Enter number: "))
# lst = [x for x in range(1, n+1) if x % 3 == 0]
# print("List of numbers divisible by 3:", lst)

# lst = []
# for i in range(n):
#     name = input("Enter name: ")
#     marks = int(input("Enter marks: "))
#     lst.append((name, marks))
# lst.sort(key=lambda x: x[1], reverse=True)
# print(lst[0])


# for i in range(n):
#     lst.append(list(map(int, input("Enter marks: ").split())))
# ans = [sum(x) for x in zip(*lst)]
# print(ans)
# def min_max(nums):
#     min_val = nums[0]
#     max_val = nums[0]
#     for n in nums:
#         if n < min_val:
#             min_val = n
#         if n > max_val:
#             max_val = n

#     return (min_val, max_val)
# nums = [5, 2, 9, 1, 7]
# mn, mx = min_max(nums)
# print
# tup = tuple(map(int, input("Enter numbers: ").split()))
# print(max(tup))
# print(min(tup))


tup1 = tuple(input("entera sentence: ").split())
print(tup1)
print("Number of words in the sentence:", len(tup1))
count = 0
for x in tup1:
    if tup1.count(x) == 1:
        print(f"'{x}' is a unique word.")
        count += 1
print(f"Total number of unique words: {count}")