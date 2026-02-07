import ast
from collections import Counter

nums_input = input("Enter a list of integers: ")
k_input = int(input("Enter K: "))

nums = ast.literal_eval(nums_input)

counts = Counter(nums)
top_k = counts.most_common(k_input)

result = [item[0] for item in top_k]

print(f"Top {k_input} most frequent elements: {result}")