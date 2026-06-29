text = ""

while True:
    print("\n===== Menu-Driven String Operations =====")
    print("1. Enter String")
    print("2. Display String")
    print("3. Convert to Uppercase")
    print("4. Convert to Lowercase")
    print("5. Reverse String")
    print("6. Find String Length")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        text = input("Enter a string: ")

    elif choice == "2":
        print("String:", text)

    elif choice == "3":
        print("Uppercase:", text.upper())

    elif choice == "4":
        print("Lowercase:", text.lower())

    elif choice == "5":
        print("Reversed String:", text[::-1])

    elif choice == "6":
        print("Length of String:", len(text))

    elif choice == "7":
        print("Program Closed.")
        break

    else:
        print("Invalid choice! Please try again.")
        