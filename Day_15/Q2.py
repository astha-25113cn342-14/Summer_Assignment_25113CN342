arr = list(map(int, input("Enter elements: ").split()))

arr = arr[1:] + arr[:1]

print("Array after left rotation:", arr)