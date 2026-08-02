# Q1
# file = open("data.txt", "w")

# file.write("Hello")

# Why is it generally a bad idea to forget file.close() here?

# Q2

# Suppose students.txt contains:

# Alice
# Bob
# Charlie

# Then you run:

# with open("students.txt", "w") as file:
#     file.write("Krithik")

# What will the file contain afterwards?

# Explain why.

# Q3

# What is the biggest advantage of using:

# with open(...)

# instead of manually calling close()?

# 💻 Coding Exercise 1

# Create a file called:

# notes.txt

with open("test.txt", 'x') as file:
    file.write("Learning Python\nNext Goal: AI Engineer")


# Write the following into it:

# Learning Python
# Next Goal: AI Engineer

# Then close the file.

# 💻 Coding Exercise 2

# Append this line to the same file:

# Practice every day.

with open("test.txt",'a') as file:
    file.write("\nPractice every day")

# 🏆 Mini Challenge

# Create a program that:

# Asks the user for their name.
# Appends the name to a file called:
# attendance.txt

# Each name should be written on a new line.

# Example:

# Krithik
# Rahul
# Alice

while True:
    name = input("Enter your Name: ")
    if name.lower() != "exit":
        with open("attendance.txt",'a') as file:
            file.write(f"{name}\n")
        print("Name added!")
    else:
        print("Thank you! Attendance done")
        break

# ⭐ Bonus Challenge

# Modify your Student Management System.

# Whenever a student is added:

# Instead of only storing it in the list,

# also append it to a file:

# students.txt

# Example:

# Krithik,91
# Rahul,85
# Alice,97

# Modified this alone in the Module 2 capstone project

student_list = "./Python & Engineering Foundations/Module 3/student_list.txt"

def add_student(name, marks):
    with open(student_list,'a') as file:
        file.write(f"{name}\t{marks}")
    print(f"Student {name} added!!!")

def list_students():
    print("Name\tMarks\n")
    content = ""
    with open(student_list,'r') as file:
        content = file.read()
    print(content)

# This is the first step toward persistent storage, which every real application needs.

