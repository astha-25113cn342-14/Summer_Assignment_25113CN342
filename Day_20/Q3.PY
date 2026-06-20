# Program to Find Row-wise Sum of a Matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

print("Row-wise Sum:")
for i in range(rows):
    row_sum = sum(matrix[i])
    print("Sum of Row", i + 1, "=", row_sum)