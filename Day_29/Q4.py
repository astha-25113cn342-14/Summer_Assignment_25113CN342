inventory = {}

while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Quantity")
    print("4. Delete Item")
    print("5. Search Item")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        item = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        inventory[item] = quantity
        print("Item added successfully.")

    elif choice == "2":
        if inventory:
            print("\nInventory:")
            for item, quantity in inventory.items():
                print(item, ":", quantity)
        else:
            print("Inventory is empty.")

    elif choice == "3":
        item = input("Enter item name to update: ")
        if item in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[item] = quantity
            print("Quantity updated.")
        else:
            print("Item not found.")

    elif choice == "4":
        item = input("Enter item name to delete: ")
        if item in inventory:
            del inventory[item]
            print("Item deleted.")
        else:
            print("Item not found.")

    elif choice == "5":
        item = input("Enter item name to search: ")
        if item in inventory:
            print(item, "Quantity:", inventory[item])
        else:
            print("Item not found.")

    elif choice == "6":
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please try again.")