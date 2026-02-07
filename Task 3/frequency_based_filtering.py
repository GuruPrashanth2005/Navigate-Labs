user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

result = [n for n in nums if nums.count(n) == 1]

print(result)