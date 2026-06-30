students = []

while True:
    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        course = input("Enter Course: ")
        students.append([roll, name, course])
        print("Student record added successfully.")

    elif choice == "2":
        if len(students) == 0:
            print("No records found.")
        else:
            print("\nRoll\tName\tCourse")
            for student in students:
                print(student[0], "\t", student[1], "\t", student[2])

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        found = False
        for student in students:
            if student[0] == roll:
                print("\nRecord Found")
                print("Roll Number:", student[0])
                print("Name:", student[1])
                print("Course:", student[2])
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        found = False
        for student in students:
            if student[0] == roll:
                student[1] = input("Enter New Name: ")
                student[2] = input("Enter New Course: ")
                print("Record updated successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "5":
        roll = input("Enter Roll Number to delete: ")
        found = False
        for student in students:
            if student[0] == roll:
                students.remove(student)
                print("Record deleted successfully.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "6":
        print("Exiting Student Record System...")
        break

    else:
        print("Invalid choice. Please try again.")