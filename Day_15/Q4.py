arr = list(map(int, input("Enter elements: ").split()))

result = [x for x in arr if x != 0] + [0] * arr.count(0)

print("Array after moving zeroes to end:", result)