input=input("enter a character: ")
if input.isdigit():
    print(f"{input} is a digit(s)")
elif input.isalpha():
    print(f"{input} is an alphabet(s)")
else:
    print(f"{input} is a special character(s)")