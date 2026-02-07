import string

user_input = input("Enter a sentence: ")

alphabet_set = set(string.ascii_lowercase)
sentence_set = set(user_input.lower())

is_pangram = alphabet_set.issubset(sentence_set)

print(f"Contains all alphabets: {is_pangram}")