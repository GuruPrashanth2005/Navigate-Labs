user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

result = []
if nums:
    result.append(nums[0])
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            result.append(nums[i])

print(result)