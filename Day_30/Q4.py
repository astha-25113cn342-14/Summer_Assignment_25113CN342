students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    students.append([roll, name, course])
    print("Student added successfully.")

def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nRoll\tName\tCourse")
        for student in students:
            print(student[0], "\t", student[1], "\t", student[2])

def search_student():
    roll = input("Enter Roll Number to search: ")
    for student in students:
        if student[0] == roll:
            print("\nRecord Found")
            print("Roll Number:", student[0])
            print("Name:", student[1])
            print("Course:", student[2])
            return
    print("Student not found.")

def update_student():
    roll = input("Enter Roll Number to update: ")
    for student in students:
        if student[0] == roll:
            student[1] = input("Enter New Name: ")
            student[2] = input("Enter New Course: ")
            print("Record updated successfully.")
            return
    print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for student in students:
        if student[0] == roll:
            students.remove(student)
            print("Record deleted successfully.")
            return
    print("Student not found.")

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")