names_input = input("Enter names separated by spaces: ")
marks_input = input("Enter marks separated by spaces: ")

names = names_input.split()
marks = [int(m) for m in marks_input.split()]

combined = list(zip(names, marks))

sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)

for i, (name, mark) in enumerate(sorted_combined):
    print(f"{name}: Rank {i + 1}")