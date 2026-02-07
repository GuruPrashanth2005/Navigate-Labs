rows = int(input("Enter number of rows: "))
matrix = []

for i in range(rows):
    row_input = input(f"Enter numbers for row {i+1} separated by spaces: ")
    matrix.append([int(x) for x in row_input.split()])

for row in matrix:
    print(max(row) if row else "Empty row")