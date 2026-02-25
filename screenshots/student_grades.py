# Student Grades
grades = {"Alice": "A", "Bob": "B"}

while True:
    print("\nOptions: 1-Add, 2-Update, 3-Print, 4-Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in grades:
            grade = input("Enter new grade: ")
            grades[name] = grade
        else:
            print("Student not found.")
    elif choice == "3":
        for student, grade in grades.items():
            print(f"{student}: {grade}")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
