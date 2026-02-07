user_input = input("Enter your string: ")

counts = {
    "alphabets": 0,
    "digits": 0,
    "special_characters": 0
}

for char in user_input:
    if char.isalpha():
        counts["alphabets"] += 1
    elif char.isdigit():
        counts["digits"] += 1
    elif not char.isspace():  # Excludes spaces from special characters
        counts["special_characters"] += 1

print(counts)