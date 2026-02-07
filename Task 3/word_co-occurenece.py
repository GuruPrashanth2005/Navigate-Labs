user_input = input("Enter a sentence: ")
words = user_input.lower().split()

bigrams = {}

for i in range(len(words) - 1):
    pair = (words[i], words[i+1])
    if pair in bigrams:
        bigrams[pair] += 1
    else:
        bigrams[pair] = 1

print(bigrams)