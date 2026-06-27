salary_records = {}

while True:
    print("\n===== Salary Management System =====")
    print("1. Add Salary Record")
    print("2. Display Salary Records")
    print("3. Search Salary Record")
    print("4. Update Salary")
    print("5. Delete Salary Record")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        basic = float(input("Enter Basic Salary: "))
        bonus = float(input("Enter Bonus: "))
        total = basic + bonus

        salary_records[emp_id] = {
            "Name": name,
            "Basic Salary": basic,
            "Bonus": bonus,
            "Total Salary": total
        }

        print("Salary record added successfully!")

    elif choice == "2":
        if len(salary_records) == 0:
            print("No salary records found.")
        else:
            print("\nSalary Records:")
            for emp_id, details in salary_records.items():
                print("----------------------------")
                print("Employee ID:", emp_id)
                print("Name:", details["Name"])
                print("Basic Salary:", details["Basic Salary"])
                print("Bonus:", details["Bonus"])
                print("Total Salary:", details["Total Salary"])

    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in salary_records:
            print("Employee Name:", salary_records[emp_id]["Name"])
            print("Basic Salary:", salary_records[emp_id]["Basic Salary"])
            print("Bonus:", salary_records[emp_id]["Bonus"])
            print("Total Salary:", salary_records[emp_id]["Total Salary"])
        else:
            print("Record not found!")

    elif choice == "4":
        emp_id = input("Enter Employee ID to update: ")
        if emp_id in salary_records:
            basic = float(input("Enter New Basic Salary: "))
            bonus = float(input("Enter New Bonus: "))
            salary_records[emp_id]["Basic Salary"] = basic
            salary_records[emp_id]["Bonus"] = bonus
            salary_records[emp_id]["Total Salary"] = basic + bonus
            print("Salary updated successfully!")
        else:
            print("Record not found!")

    elif choice == "5":
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in salary_records:
            del salary_records[emp_id]
            print("Salary record deleted successfully!")
        else:
            print("Record not found!")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")