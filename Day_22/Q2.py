# Program to count words in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()
count = len(words)

print("Number of words =", count)