arr1 = list(map(int, input("Enter elements of first array: ").split()))

arr2 = list(map(int, input("Enter elements of second array: ").split()))

common = []

for element in arr1:
    if element in arr2 and element not in common:
        common.append(element)

print("Common elements:", common)