arr = [10, 20, 30, 20, 40, 20, 50]

key = int(input("Enter element: "))

count = 0

for i in arr:
    if i == key:arr = [10, 20, 30, 20, 40, 20, 50]

key = int(input("Enter element: "))

count = 0

for i in arr:
    if i == key:
        count += 1
print("Frequency of", key, "is", count)
count += 1

print("Frequency of", key, "is", count)