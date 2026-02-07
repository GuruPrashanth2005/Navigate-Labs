user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

leaders = []
if nums:
    current_max = nums[-1]
    leaders.append(current_max)
    
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] > current_max:
            current_max = nums[i]
            leaders.append(current_max)


print(leaders[::-1])