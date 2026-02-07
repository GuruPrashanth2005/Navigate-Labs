import ast

user_input = input("Enter a 2D list (e.g., [[1, 2, 3], [4, 5, 4]]): ")
matrix = ast.literal_eval(user_input)

def check_unique_rows(mat):
    results = []
    for i, row in enumerate(mat):
        is_unique = len(row) == len(set(row))
        results.append((i, is_unique))
    return results

row_status = check_unique_rows(matrix)

for index, unique in row_status:
    status = "Unique" if unique else "Contains Duplicates"
    print(f"Row {index}: {status}")