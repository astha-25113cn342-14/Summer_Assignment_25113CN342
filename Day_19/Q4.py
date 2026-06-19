n = int(input("Enter the order of matrix: "))

print("Enter matrix elements:")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]

print("Sum of diagonal elements =", diagonal_sum)
