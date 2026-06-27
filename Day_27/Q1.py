students = {}

while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        students[roll] = {"Name": name, "Marks": marks}
        print("Student record added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nStudent Records:")
            for roll, details in students.items():
                print("Roll No:", roll)
                print("Name:", details["Name"])
                print("Marks:", details["Marks"])
                print("----------------------")

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        if roll in students:
            print("Student Found:")
            print("Name:", students[roll]["Name"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll Number to delete: ")
        if roll in students:
            del students[roll]
            print("Student record deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")