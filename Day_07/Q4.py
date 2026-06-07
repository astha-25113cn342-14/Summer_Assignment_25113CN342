def reverse_number(n, rev=0):
    # Base case
    if n == 0:
        return rev

    # Recursive case
    return reverse_number(n // 10, rev * 10 + n % 10)

# Input from user
num = int(input("Enter a number: "))

print("Reversed number =", reverse_number(abs(num)))