user_input = input("Enter numbers separated by spaces: ")
nums = [float(x) for x in user_input.split()]

def get_stats(numbers):
    if not numbers:
        return None
    
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    
    return (minimum, maximum, average)

result = get_stats(nums)
print(result)