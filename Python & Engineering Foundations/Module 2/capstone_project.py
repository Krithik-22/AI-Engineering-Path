# 🏆 Project: Student Management System (CLI)

# You'll build a console application that lets a user:

# Add students
# View all students
# Search for a student
# Calculate average marks
# Show highest and lowest marks
# Display Pass/Fail status
# Use functions to organize the code
# Use loops for the menu
# Use conditions for decisions
# Use dictionaries/lists to store data
# Use return where appropriate
# Use lambda to sort students by marks

# This project will feel much closer to something you'd build at work.

menu = """
Welcome to the Student Management System (CLI)
----------------------------------------------
1. Add a Student
2. View all Students
3. Search for a Student
4. calculate average marks
5. Show highest and lowest marks
6. Display Student result status
7. Exit
"""

students = []

def add_student(name, marks):
    students.append((name, marks))
    return students

def list_students():
    print("Name\tMarks\n")
    for student in students:
        print(f"{student[0]}\t{student[1]}")

def search_student(stud):
    for idx, student in enumerate(students):
        if stud == student[0]:
            return idx
    return -1

def calculate_average_marks():
    marks = list(map(lambda student : student[1], students))
    return sum(marks)/len(marks)
    

def highest_mark():
    top_mark = max(list(map(lambda student : student[1], students)))
    top_student = list(filter(lambda student : student[1] == top_mark, students))
    return top_student

def lowest_mark():
    low_mark = min(list(map(lambda student : student[1], students)))
    bottom_student = list(filter(lambda student : student[1] == low_mark, students))
    return bottom_student

def display_student_result():
    print(f"Student\tMark\tResult")
    for student, mark in students:
        result = "Pass" if mark >= 35 else "Fail"
        print(f"{student}\t{mark}\t{result}")

while True:
    print(menu)
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
         print("Invalid choice. Please enter a number.")
         continue

    if choice == 1:
        student = input("Enter Student Name: ")
        mark = int(input("Enter Student Marks: "))
        add_student(student, mark)
        print("Student added!!!")
    elif choice == 2:
        list_students()
    elif choice == 3:
        student_to_search = input("Enter the Student name you would like to search: ")
        result = search_student(student_to_search)
        if result >= 0:
            print(f"{student_to_search} found at index {result}")
        else:
            print("Student not found!!!") 
    elif choice == 4:
        avg_marks = calculate_average_marks()
        print(f"Average Marks of the students: {avg_marks}")
    elif choice == 5:
        top_mark = highest_mark()
        bottom_mark = lowest_mark()
        print(f"Highest Mark: {top_mark}\nLowest Mark: {bottom_mark}")
    elif choice == 6:
        display_student_result()
    elif choice == 7:
        break
    else:
        print("Invalid Choice. Try Again!!!")