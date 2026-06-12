# Input size of array
n = int(input("Enter number of elements: "))

# Input array elements
arr = []
for i in range(n):
    arr.append(int(input()))

# Count even and odd elements
even = 0
odd = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

# Display result
print("Even elements =", even)
print("Odd elements =", odd)