user_input = input("Enter your nested list (e.g., [[1,2],[3,4],[5]]): ")

# Remove brackets and spaces, then split by commas
clean_input = user_input.replace("[", "").replace("]", "").replace(" ", "")
flat_list = [int(x) for x in clean_input.split(",") if x]

print(flat_list)