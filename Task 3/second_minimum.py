user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

first = second = float('inf')
for n in nums:
    if n < first:
        first, second = n, first
    elif first < n < second:
        second = n

print(second if second != float('inf') else "No second smallest found")