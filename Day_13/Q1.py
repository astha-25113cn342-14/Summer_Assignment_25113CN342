n = int(input("Enter number of elements: "))

# Input array elements
arr = []
for i in range(n):
    arr.append(int(input()))

# Display array
print("Array elements are:")
for i in arr:
    print(i, end=" ")