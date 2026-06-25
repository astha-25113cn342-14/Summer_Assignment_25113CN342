# ATM Simulation

balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful.")

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    elif choice == 4:
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice.")