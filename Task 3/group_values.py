user_input = input("Enter marks separated by spaces: ")
marks = [int(m) for m in user_input.split()]

categories = {
    "<50": [],
    "50–74": [],
    ">=75": []
}

for mark in marks:
    if mark < 50:
        categories["<50"].append(mark)
    elif 50 <= mark <= 74:
        categories["50–74"].append(mark)
    else:
        categories[">=75"].append(mark)

print(categories)