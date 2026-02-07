user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

def has_duplicates(numbers):
    return len(numbers) != len(set(numbers))

if has_duplicates(nums):
    print("Duplicates detected.")
else:
    print("No duplicates found.")