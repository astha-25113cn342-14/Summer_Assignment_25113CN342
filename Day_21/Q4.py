string = input("Enter a lowercase string: ")

uppercase_string = ""

for char in string:
    if 'a' <= char <= 'z':
        uppercase_string += chr(ord(char) - 32)
    else:
        uppercase_string += char

print("Uppercase string:", uppercase_string)