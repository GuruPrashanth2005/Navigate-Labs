rows = int(input("Enter number of rows: "))
matrix = []

for i in range(rows):
    row_input = input(f"Enter numbers for row {i+1} separated by spaces: ")
    matrix.append([int(x) for x in row_input.split()])

if matrix and matrix[0]:
    num_cols = len(matrix[0])
    for j in range(num_cols):
        col_sum = sum(row[j] for row in matrix)
        print(f"Column {j+1} sum: {col_sum}")