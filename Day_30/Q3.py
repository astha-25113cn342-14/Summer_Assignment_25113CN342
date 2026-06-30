employees = []

while True:
    print("\n===== Mini Employee Management System =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        employees.append([emp_id, name, department])
        print("Employee added successfully.")

    elif choice == "2":
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nID\tName\tDepartment")
            for emp in employees:
                print(emp[0], "\t", emp[1], "\t", emp[2])

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")
        found = False
        for emp in employees:
            if emp[0] == emp_id:
                print("\nEmployee Found")
                print("ID:", emp[0])
                print("Name:", emp[1])
                print("Department:", emp[2])
                found = True
                break
        if not found:
            print("Employee not found.")

    elif choice == "4":
        emp_id = input("Enter Employee ID to update: ")
        found = False
        for emp in employees:
            if emp[0] == emp_id:
                emp[1] = input("Enter New Name: ")
                emp[2] = input("Enter New Department: ")
                print("Employee record updated successfully.")
                found = True
                break
        if not found:
            print("Employee not found.")

    elif choice == "5":
        emp_id = input("Enter Employee ID to delete: ")
        found = False
        for emp in employees:
            if emp[0] == emp_id:
                employees.remove(emp)
                print("Employee record deleted successfully.")
                found = True
                break
        if not found:
            print("Employee not found.")

    elif choice == "6":
        print("Exiting Employee Management System...")
        break

    else:
        print("Invalid choice. Please try again.")