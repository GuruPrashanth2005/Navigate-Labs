letter=input("Enter an alphabet: ").strip().lower()
if letter in 'aeiou' and len(letter) == 1:
    print(f"{letter} is a vowel")
elif len(letter)>1:
    print("Enter only a single alphabet")
else:       
    print(f"{letter} is a consonant")