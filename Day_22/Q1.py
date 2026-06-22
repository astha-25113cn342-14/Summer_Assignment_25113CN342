# Program to check palindrome string

s = input("Enter a string: ")

if s == s[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")