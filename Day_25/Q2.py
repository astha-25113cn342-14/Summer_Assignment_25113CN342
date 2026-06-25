# Program to find common characters in two strings

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

common = set(str1) & set(str2)

print("Common characters:", "".join(common))