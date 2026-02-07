data_input = input("Enter the data list (separated by spaces): ")
remove_input = input("Enter the elements to remove (separated by spaces): ")

data = data_input.split()
remove_list = set(remove_input.split())

filtered_data = [item for item in data if item not in remove_list]

print(filtered_data)