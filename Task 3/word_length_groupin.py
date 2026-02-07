import ast

user_input = input("Enter a list of words: ")
words = ast.literal_eval(user_input)

grouped_words = {}

for word in words:
    length = len(word)
    if length not in grouped_words:
        grouped_words[length] = []
    grouped_words[length].append(word)

print(grouped_words)