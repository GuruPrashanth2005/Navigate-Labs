user_input = input("Enter your paragraph: ")

words = user_input.lower().split()

cleaned_words = [word.strip('.,!?;:"()') for word in words]
unique_words = set(w for w in cleaned_words if w)

print(len(unique_words))