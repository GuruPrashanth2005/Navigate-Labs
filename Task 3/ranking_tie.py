import ast

user_input = input("Enter list of tuples (name, score): ")
data = ast.literal_eval(user_input)

sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

ranked_results = []
current_rank = 1

for i in range(len(sorted_data)):
    if i > 0 and sorted_data[i][1] < sorted_data[i-1][1]:
        current_rank = i + 1
    
    ranked_results.append((sorted_data[i][0], sorted_data[i][1], current_rank))

print("Ranks:")
for name, score, rank in ranked_results:
    print(f"{name}: {score} -> Rank {rank}")