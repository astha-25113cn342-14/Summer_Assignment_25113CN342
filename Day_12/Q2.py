def armstrong(n):
    digits = len(str(n))
    total = sum(int(digit) ** digits for digit in str(n))
    return total == n

# Input
num = int(input("Enter a number: "))

if armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")