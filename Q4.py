string = input("Enter a string: ")

max_char = string[0]
max_count = string.count(max_char)

for ch in string:
    count = string.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch

print("Maximum occurring character:", max_char)
print("Frequency:", max_count)