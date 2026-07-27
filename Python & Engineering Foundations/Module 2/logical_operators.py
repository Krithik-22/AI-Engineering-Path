# Instead of asking "What does this print?", let's ask "Why?"

# Question 1
# age = 20
# has_id = False

# if age >= 18 and has_id:
#     print("Allowed")
# else:
#     print("Denied")

# Why is the output what it is?

# Question 2
# role = "developer"

# if role in ("admin", "developer"):
#     print("Access")

# Why is in cleaner than using multiple or conditions?


# Question 3
# logged_in = False

# if not logged_in:
#     print("Login Required")

# Why does not make this easier to read than writing an equality check?

# 💻 Coding Exercise

# Build a Login Validator.

# Requirements:

# Ask the user for:

# Username
# Password

# Rules:

# Username: admin
# Password: python123

# If both are correct:

# Login Successful

# Otherwise:

# Invalid Credentials

# 👉 Use the and operator.

username = input("Enter your username : ")
password = input("Enter your password : ")

if username == 'admin' and password == 'python123':
    print("Login Successful")
else:
    print('Invalid Credentials')

# 🏆 Mini Challenge

# Build a Scholarship Eligibility Checker.

# Ask for:

# Age
# Marks (out of 100)
# Family income (₹ per year)

# Rules:

# Eligible if:
# Marks are 90 or above
# AND family income is less than ₹500000
# AND age is 25 or below

# Otherwise:

# Not Eligible
# Bonus Challenge ⭐

# Instead of writing one giant if, create meaningful boolean variables first.

age = int(input("Enter your age : "))
marks = int(input("Enter your Marks (out of 100) : "))
family_income = int(input("Enter your family income (₹ per year) : "))

good_marks = marks >= 90
low_income = family_income < 500000
eligible_age = age <= 25

if good_marks and low_income and eligible_age:
    print("Eligible for Scholarship")
else:
    print("Not eligible")

# For example:

# good_marks = marks >= 90
# low_income = income < 500000
# eligible_age = age <= 25

# Then combine them.

# This is how experienced developers write complex conditions because it's much easier to read and debug.

