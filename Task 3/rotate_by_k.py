user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]
k = int(input("Enter K: "))

k = k % len(nums) if nums else 0
result = nums[-k:] + nums[:-k]

print(result)