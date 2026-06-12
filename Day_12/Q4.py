
def perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n

# Input
num = int(input("Enter a number: "))

if perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")