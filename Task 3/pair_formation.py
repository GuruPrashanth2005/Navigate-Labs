user_input = input("Enter numbers separated by spaces: ")
nums = [int(x) for x in user_input.split()]

squared_tuples = [(n, n**2) for n in nums]

print(squared_tuples)