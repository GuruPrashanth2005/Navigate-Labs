user_input = input("Enter a number: ")

all_digits = set("0123456789")

present_digits = set(user_input)

missing_digits = sorted(list(all_digits - present_digits))

print("Missing digits:", ", ".join(missing_digits) if missing_digits else "None")