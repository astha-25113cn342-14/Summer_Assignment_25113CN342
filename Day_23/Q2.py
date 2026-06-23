string = input("Enter a string: ")

seen = set()

for ch in string:
    if ch in seen:
        print("First repeating character:", ch)
        break
    seen.add(ch)
else:
    print("No repeating character found")