# Q1

# What happens here?

# try:
#     number = int("abc")
#     print("Hello")
# except ValueError:
#     print("Invalid number")

# What gets printed, and why doesn't "Hello" get printed?

# Q1: Invalid number
# Q2: IndexError. ouput is Invalid index
# Q3: the first handles a specific exception whereas the secind handles everything even if there was something that wasn't intended to be handled.

# Q2

# What exception occurs here?

# numbers = [10, 20, 30]


# try:
#     print(numbers[5])
# except IndexError:
#     print("Invalid index")
# Q3

# What's the difference between:

# except ValueError:

# and:

# except:

# Why is the first generally preferred?

# 💻 Coding Exercise 1

# Create a program that asks:

# Enter a number:

# Convert it to an integer.

# If the user enters something invalid, print:

# Invalid input. Please enter a number.

# Use try and except.

try:
    num = int(input("Enter a number: "))
    print(f'The entered number is {num}')
except ValueError:
    print('Please enter a valid number.')


# 💻 Coding Exercise 2

# Create a calculator that asks for:

# Number 1
# Number 2

# Then divides them.

# Your program should handle:

# Non-numeric input → "Please enter numbers only."
# Division by zero → "Cannot divide by zero."

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    div = num1/num2
except ValueError:
    print('Please enter numbers only')
except ZeroDivisionError:
    print("Cannot divide by zero")

# 🏆 Mini Challenge

# Remember your attendance program?

# Currently:

# name = input("Enter your Name: ")

# Suppose the user enters nothing.

# Modify the program so that an empty name produces:

# Name cannot be empty.

# Then ask again.
while True:
    name = input("Enter your Name: ")
    if len(name) == 0:
        print("Name cannot be empty")
        pass
    elif name.lower() != "exit":
        with open("attendance.txt",'a') as file:
            file.write(f"{name}\n")
        print("Name added!")
    else:
        print("Thank you! Attendance done")
        break

# ⭐ Bonus Challenge — Your Student Management System

# This is where I want you to apply the lesson to your previous project.

# Currently:

# choice = int(input("Enter your choice: "))

# If the user enters:

# abc

# your entire application crashes.

# Modify it so:

# Enter your choice: abc


# Invalid choice. Please enter a number.

# and the application continues running.

# Also handle this:

# Enter Student Marks: abc

# without crashing.

while True:
    try:
        print("#menu")
        choice = int(input("Enter your choice: "))
    except ValueError:
            print("Invalid choice. Please enter a number.")
    #rest of the method calls here. Updated in the capstome project of module 2