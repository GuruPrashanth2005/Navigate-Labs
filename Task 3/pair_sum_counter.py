user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]
k = int(input("Enter target value K: "))

count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == k:
            count += 1

print(count)