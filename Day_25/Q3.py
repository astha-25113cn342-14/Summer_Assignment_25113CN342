# Program to sort names alphabetically

names = input("Enter names separated by space: ").split()

names.sort()

print("Sorted names:")
for name in names:
    print(name)