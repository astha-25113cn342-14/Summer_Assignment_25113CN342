arr = []

while True:
    print("\n===== Menu-Driven Array Operations =====")
    print("1. Create Array")
    print("2. Display Array")
    print("3. Insert Element")
    print("4. Delete Element")
    print("5. Search Element")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        n = int(input("Enter number of elements: "))
        arr = []
        for i in range(n):
            arr.append(int(input(f"Enter element {i + 1}: ")))

    elif choice == "2":
        print("Array:", arr)

    elif choice == "3":
        element = int(input("Enter element to insert: "))
        arr.append(element)
        print("Element inserted.")

    elif choice == "4":
        element = int(input("Enter element to delete: "))
        if element in arr:
            arr.remove(element)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif choice == "5":
        element = int(input("Enter element to search: "))
        if element in arr:
            print("Element found at index", arr.index(element))
        else:
            print("Element not found.")

    elif choice == "6":
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please try again.")