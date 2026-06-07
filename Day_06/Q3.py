n = int(input("Enter a number: "))

count = bin(n).count('1')

print("Number of set bits:", count)