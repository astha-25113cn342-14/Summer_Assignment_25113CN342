# Program to Multiply Two Matrices

# Input matrix A
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

A = []
print("Enter elements of first matrix:")
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

# Input matrix B
r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

B = []
print("Enter elements of second matrix:")
for i in range(r2):
    row = list(map(int, input().split()))
    B.append(row)

# Check if multiplication is possible
if c1 != r2:
    print("Matrix multiplication not possible!")
else:
    result = [[0 for j in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix:")
    for row in result:
        print(*row)