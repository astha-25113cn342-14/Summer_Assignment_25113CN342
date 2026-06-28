tickets = []

while True:
    print("\nTicket Booking System")
    print("1. Book Ticket")
    print("2. View Booked Tickets")
    print("3. Search Ticket")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ticket_id = input("Enter Ticket ID: ")
        name = input("Enter Passenger Name: ")
        destination = input("Enter Destination: ")

        tickets.append({
            "id": ticket_id,
            "name": name,
            "destination": destination
        })

        print("Ticket booked successfully.")

    elif choice == "2":
        if not tickets:
            print("No tickets booked.")
        else:
            print("\nBooked Tickets:")
            for ticket in tickets:
                print(f"Ticket ID: {ticket['id']}")
                print(f"Passenger Name: {ticket['name']}")
                print(f"Destination: {ticket['destination']}")
                print()

    elif choice == "3":
        ticket_id = input("Enter Ticket ID to search: ")
        found = False

        for ticket in tickets:
            if ticket["id"] == ticket_id:
                print("\nTicket Found:")
                print(f"Ticket ID: {ticket['id']}")
                print(f"Passenger Name: {ticket['name']}")
                print(f"Destination: {ticket['destination']}")
                found = True
                break

        if not found:
            print("Ticket not found.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")