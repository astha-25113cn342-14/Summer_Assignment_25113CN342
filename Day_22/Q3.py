# Program to find character frequency in a string

s = input("Enter a string: ")

for ch in set(s):
    print(ch, ":", s.count(ch))