books = []

while True:
    print("\n===== Mini Library System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        books.append([book_id, title, author, "Available"])
        print("Book added successfully.")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\nID\tTitle\tAuthor\tStatus")
            for book in books:
                print(book[0], "\t", book[1], "\t", book[2], "\t", book[3])

    elif choice == "3":
        title = input("Enter Book Title to search: ")
        found = False
        for book in books:
            if book[1].lower() == title.lower():
                print("\nBook Found")
                print("Book ID:", book[0])
                print("Title:", book[1])
                print("Author:", book[2])
                print("Status:", book[3])
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "4":
        title = input("Enter Book Title to issue: ")
        found = False
        for book in books:
            if book[1].lower() == title.lower():
                if book[3] == "Available":
                    book[3] = "Issued"
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "5":
        title = input("Enter Book Title to return: ")
        found = False
        for book in books:
            if book[1].lower() == title.lower():
                if book[3] == "Issued":
                    book[3] = "Available"
                    print("Book returned successfully.")
                else:
                    print("Book is already available.")
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "6":
        print("Exiting Mini Library System...")
        break

    else:
        print("Invalid choice. Please try again.")