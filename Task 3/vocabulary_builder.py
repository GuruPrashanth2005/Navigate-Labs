import re

print("Enter your sentences (type 'DONE' or leave blank to finish):")
sentences = []

while True:
    line = input("> ")
    if line.upper() == "DONE" or line == "":
        break
    sentences.append(line)

all_text = " ".join(sentences).lower()
unique_words = set(re.findall(r'\b\w+\b', all_text))

print("\nTotal unique words found:", len(unique_words))
print(sorted(list(unique_words)))