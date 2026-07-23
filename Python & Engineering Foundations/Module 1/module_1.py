# Build a small Developer Profile Generator.

# Requirements:

# Ask for:
# Name
# Company
# Role
# Years of Experience
# Favorite Programming Language
# Print a clean profile like:
# ===== Developer Profile =====
# Name      : Krithik
# Company   : Kaleris
# Role      : Associate Support Engineer
# Experience: 1 year
# Language  : Python

# Future Goal:
# Become an AI Engineer 🚀

# Use:

# input()
# int() where appropriate
# f-strings
# clear variable names

# name = input("Enter your Name: ")
# company = input("Enter your Company name: ")
# role = input("Enter your role in your company: ")
# years_of_experience = input("Enter your years of experience: ")
# fav_prog_lang = input("Enter your favorite programming language: ")

# print(f"""
# ==== Developer Profile ====\nName:  {name}\nCompany:   {company}\nRole:   {role}\nExperience: {years_of_experience} year\nLanguage: {fav_prog_lang}\n
# """)
# print(f"Future goal: \nBecome an AI Engineer")

# Write a program that:

# Takes two numbers as input.
# Prints:
# Sum
# Difference
# Product
# Division
# Floor Division
# Modulus
# Power (num1 ** num2)
# Checks:
# Are the numbers equal?
# Is the first number greater?
# Is the first number even? 
# Print everything using f-strings.

num_1 = int(input("Enter Number 1: "))
num_2 = int(input("Enter Number 2: "))

print(f"""
Sum         : {num_1 + num_2}
Difference  : {num_1 - num_2}
Product     : {num_1 * num_2}
Division    : {num_1/num_2}
Floor Division: {num_1//num_2}
Modulus     : {num_1 % num_2}
Power       : {num_1 ** num_2}
""")

if num_1 == num_2:
    print(f"{num_1} and {num_2} are equal")
elif num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_1 < num_2:
    print(f"{num_1} is lesser than {num_2}")