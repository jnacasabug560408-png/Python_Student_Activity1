import csv
import os

# ===== Global Data =====
students = {}  # Key = student_id, Value = { 'name': str, 'age': int, 'grades': list }
file_name = "students.csv"


# ===== Function Definitions =====

def add_student(student_id, name, age, *grades):
    if student_id in students:
        print("Student ID already exists.")
        return
    students[student_id] = {
        'name': name,
        'age': age,
        'grades': list(grades)
    }
    print(f"Student {name} added successfully.\n")


def display_students(from_file=False):
    if from_file:
        print("=== Students From File ===")
        if not os.path.exists(file_name):
            print("File does not exist.\n")
            return
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        print()
        return

    print("=== Students in Memory ===")
    for sid, info in students.items():
        student_tuple = (sid, info['name'])  # Tuple for fixed info
        print(f"ID: {student_tuple[0]}, Name: {student_tuple[1]}, Age: {info['age']}")
        print("Grades: ", end="")
        for grade in info['grades']:  # Nested loop
            print(grade, end=" ")
        print("\n")
    if not students:
        print("No students to display.\n")


def update_student(student_id):
    if student_id not in students:
        print("Student not found.\n")
        return

    print("Leave blank to keep current value.")
    new_name = input("Enter new name: ")
    new_age = input("Enter new age: ")

    if new_name:
        students[student_id]['name'] = new_name
    if new_age.isdigit():
        students[student_id]['age'] = int(new_age)

    grades_input = input("Enter new grades separated by space (or leave blank): ")
    if grades_input:
        new_grades = list(map(int, grades_input.split()))
        students[student_id]['grades'] = new_grades

    print("Student updated successfully.\n")


def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student {student_id} deleted successfully.\n")
    else:
        print("Student not found.\n")


def save_to_file(filename=file_name):  # Default argument
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for sid, info in students.items():
            row = [sid, info['name'], info['age']] + info['grades']
            writer.writerow(row)
    print("Data saved to file successfully.\n")


def load_from_file():
    if not os.path.exists(file_name):
        print("File not found.\n")
        return

    students.clear()  # Reset current data
    with open(file_name, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            sid = row[0]
            name = row[1]
            age = int(row[2])
            grades = list(map(int, row[3:]))
            students[sid] = {
                'name': name,
                'age': age,
                'grades': grades
            }
    print("Data loaded from file.\n")


# Demonstration of lambda and variable scopes
average_grade = lambda grades: sum(grades) / len(grades) if grades else 0


# ===== Main Program =====

def main():
    load_from_file()  # Load data at start

    while True:
        print("===== Student Information System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if not choice.isdigit():
            print("Invalid input. Try again.\n")
            continue  # Loop again

        choice = int(choice)

        if choice == 1:
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grades_input = input("Enter grades separated by space: ")
            grades = list(map(int, grades_input.split()))
            add_student(sid, name, age, *grades)

        elif choice == 2:
            sub_choice = input("Display from file? (y/n): ")
            if sub_choice.lower() == 'y':
                display_students(from_file=True)
            else:
                display_students()

        elif choice == 3:
            sid = input("Enter Student ID to update: ")
            update_student(sid)

        elif choice == 4:
            sid = input("Enter Student ID to delete: ")
            delete_student(sid)

        elif choice == 5:
            save_to_file()

        elif choice == 6:
            load_from_file()

        elif choice == 7:
            print("Exiting program.")
            break  # Exit the loop

        else:
            print("Invalid choice. Try again.\n")


# ===== Entry Point =====
if __name__ == "__main__":
    main()
