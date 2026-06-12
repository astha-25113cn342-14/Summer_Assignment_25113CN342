# Input size of array
n = int(input("Enter number of elements: "))

# Input array elements
arr = []
for i in range(n):
    arr.append(int(input()))

# Find largest and smallest element
largest = max(arr)
smallest = min(arr)

# Display result
print("Largest element =", largest)
print("Smallest element =", smallest)