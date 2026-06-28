books = []

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        books.append({
            "id": book_id,
            "title": title,
            "author": author
        })

        print("Book added successfully.")

    elif choice == "2":
        if not books:
            print("No books available.")
        else:
            print("\nLibrary Books:")
            for book in books:
                print(f"Book ID: {book['id']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print()

    elif choice == "3":
        title = input("Enter Book Title to Search: ")
        found = False

        for book in books:
            if book["title"].lower() == title.lower():
                print("\nBook Found:")
                print(f"Book ID: {book['id']}")
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                found = True
                break

        if not found:
            print("Book not found.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")