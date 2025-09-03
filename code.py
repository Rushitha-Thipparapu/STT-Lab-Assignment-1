"""This program calculates total, average, pass/fail, and grade for students."""

students = [
    {"name": "Rishi", "age": 20, "marks": [78, 85, 92, 67, 88]},
    {"name": "Hari", "age": 21, "marks": [6, 4, 1, 9, 19]}
]

for student in students:
    print("Student Name:", student["name"])
    print("Student Age:", student["age"])

    total = sum(student["marks"])
    average = total / len(student["marks"])

    print("Marks:", student["marks"])
    print("Total Marks:", total)
    print("Average Marks:", average)

    if average >= 50:
        print(student["name"], "has passed")
    else:
        print(student["name"], "has failed")

    if average >= 90:
        student_grade = "A+"
    elif average >= 75:
        student_grade = "A"
    elif average >= 60:
        student_grade = "B"
    elif average >= 50:
        student_grade = "C"
    else:
        student_grade = "F"

    print("Grade:", student_grade)
    print("-" * 30)

print("Program finished")
