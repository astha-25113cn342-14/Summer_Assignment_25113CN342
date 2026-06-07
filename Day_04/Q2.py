n = int(input("Enter the value of n: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("The 1st Fibonacci term is:", a)
else:
    for i in range(2, n + 1):
        a, b = b, a + b
    print(f"The {n}th Fibonacci term is:", a)