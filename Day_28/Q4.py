contacts = []

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })

        print("Contact added successfully.")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for contact in contacts:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print()

    elif choice == "3":
        name = input("Enter Name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print("\nContact Found:")
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                found = True
                break

        if not found:
            print("Contact not found.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")