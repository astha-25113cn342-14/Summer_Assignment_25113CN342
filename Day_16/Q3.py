arr = [1, 4, 5, 6, 3, 2]
target = 7

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair:", arr[i], arr[j])