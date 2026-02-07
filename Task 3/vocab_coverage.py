import ast
import re

vocab_input = input("Enter expected vocabulary words (as a list or set): ")
docs_input = input("Enter list of documents (sentences): ")

expected_vocab = {word.strip().lower() for word in ast.literal_eval(vocab_input)}
documents = ast.literal_eval(docs_input)

found_words = set()
for doc in documents:
    words = re.findall(r'\b\w+\b', doc.lower())
    found_words.update(words)

covered_words = expected_vocab.intersection(found_words)
missing_words = expected_vocab - found_words

coverage_percentage = (len(covered_words) / len(expected_vocab)) * 100 if expected_vocab else 0

print(f"\nPercentage of vocabulary covered: {coverage_percentage}%")
print(f"Missing words: {missing_words}")