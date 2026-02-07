user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

def split_even_odd(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    odds = [n for n in numbers if n % 2 != 0]
    return evens, odds

even_list, odd_list = split_even_odd(nums)

print("Evens:", even_list)
print("Odds:", odd_list)