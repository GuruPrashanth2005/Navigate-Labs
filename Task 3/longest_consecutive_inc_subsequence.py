user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

def find_longest_increasing(nums):
    if not nums:
        return 0
    
    max_length = 1
    current_streak = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current_streak += 1
        else:
            max_length = max(max_length, current_streak)
            current_streak = 1
            
    return max(max_length, current_streak)

print(find_longest_increasing(nums))