# 🏋️ Coding Exercise

# Write a program that:

# Takes a user's age as input.
# If age is:
# less than 13 → print "Child"
# 13–19 → print "Teenager"
# 20–59 → print "Adult"
# 60 and above → print "Senior Citizen"

# Use if, elif, and else.

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# 🏆 Mini Challenge

# Create a Movie Ticket Eligibility Checker.

# Ask the user:

# Age
# Has student ID? (yes/no)

# Rules:

# Under 5 → Free ticket
# 5–17 → Child ticket
# 18–59:
# Student → Student discount
# Otherwise → Regular ticket
# 60+ → Senior discount

age = int(input("Enter your age: "))
has_student_id = input("Do you have a Student ID: ")

if age < 5:
    print("Free ticket")
elif age < 18:
    print("Child ticket")
elif age < 60:
    if has_student_id:
        print("Student discount")
    else:
        print("Regular ticket")
else:
    print("Senior discount")