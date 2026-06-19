rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of the matrix:")
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transpose of the matrix:")
for row in transpose:
    print(*row)