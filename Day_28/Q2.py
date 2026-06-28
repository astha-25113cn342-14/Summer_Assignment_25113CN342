account = {}

while True:
    print("\nBank Account System")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account["number"] = input("Enter Account Number: ")
        account["name"] = input("Enter Account Holder Name: ")
        account["balance"] = float(input("Enter Initial Balance: "))
        print("Account created successfully.")

    elif choice == "2":
        if account:
            amount = float(input("Enter amount to deposit: "))
            account["balance"] += amount
            print("Amount deposited successfully.")
        else:
            print("Create an account first.")

    elif choice == "3":
        if account:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= account["balance"]:
                account["balance"] -= amount
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Create an account first.")

    elif choice == "4":
        if account:
            print("\nAccount Details")
            print("Account Number:", account["number"])
            print("Account Holder:", account["name"])
            print("Balance:", account["balance"])
        else:
            print("No account found.")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")