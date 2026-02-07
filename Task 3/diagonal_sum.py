import ast

user_input = input("Enter a square matrix (e.g., [[1,2],[3,4]]): ")
matrix = ast.literal_eval(user_input)

def calculate_diagonals(mat):
    n = len(mat)
    primary_sum = 0
    secondary_sum = 0
    
    for i in range(n):
        primary_sum += mat[i][i]
        secondary_sum += mat[i][n - 1 - i]
        
    return primary_sum, secondary_sum

p_sum, s_sum = calculate_diagonals(matrix)

print(f"Primary Diagonal Sum: {p_sum}")
print(f"Secondary Diagonal Sum: {s_sum}")