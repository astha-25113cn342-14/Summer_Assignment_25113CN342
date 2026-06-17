arr1 = list(map(int, input("Enter elements of first array: ").split()))

arr2 = list(map(int, input("Enter elements of second array: ").split()))

union_array = list(set(arr1) | set(arr2))

print("Union of arrays:", union_array)