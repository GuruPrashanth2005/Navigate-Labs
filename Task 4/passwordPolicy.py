passwords = eval(input("Passwords (list): "))
valid = [p for p in passwords if any(c.isdigit() for c in p) and any(c in "!@#$%^&*" for c in p)]
invalid = [p for p in passwords if p not in valid]
print(f"Valid: {valid}")
print(f"Invalid: {invalid}")