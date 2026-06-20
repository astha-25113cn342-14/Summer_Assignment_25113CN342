# Program to Check Symmetric Matrix

n = int(input("Enter the order of matrix: "))

matrix = []
print("Enter matrix elements:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

if symmetric:
    print("The matrix is Symmetric.")
else:
    print("The matrix is Not Symmetric.")