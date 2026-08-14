# Student Result Management System

students = {
    "Rahul": [78, 85, 69],
    "Priya": [92, 88, 95],
    "Amit": [55, 63, 48],
    "Sneha": [81, 74, 89]
}

def calculate_result(name, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    return total, average, grade


def display_result(name, marks):
    total, average, grade = calculate_result(name, marks)

    print("\nStudent Name:", name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)

    if grade == "F":
        print("Status: Failed")
    else:
        print("Status: Passed")


print("===== STUDENT RESULT SYSTEM =====")
print("Available students:")

for student in students:
    print("-", student)

search_name = input("\nEnter student name: ")

if search_name in students:
    display_result(search_name, students[search_name])
else:
    print("Student not found")

choice = input("\nDo you want to see the class average? (yes/no): ")

if choice == "yes":
    total_marks = 0
    total_subjects = 0

    for marks in students.values():
        total_marks += sum(marks)
        total_subjects += len(marks)

    class_average = total_marks / total_subjects
    print("Class Average:", round(class_average, 2))

print("Program finished successfully!")
