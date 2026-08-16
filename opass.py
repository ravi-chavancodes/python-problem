students = {}

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
    else:
        for name, marks in students.items():
            print(f"{name}: {marks}")

def search_student():
    name = input("Enter name to search: ")
    if name in students:
        print(f"{name}'s Marks: {students[name]}")
    else:
        print("Student not found.")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid choice")