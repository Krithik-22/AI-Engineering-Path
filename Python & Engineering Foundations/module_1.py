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

name = input("Enter your Name: ")
company = input("Enter your Company name: ")
role = input("Enter your role in your company: ")
years_of_experience = input("Enter your years of experience: ")
fav_prog_lang = input("Enter your favorite programming language: ")

print(f"""
==== Developer Profile ====\nName:  {name}\nCompany:   {company}\nRole:   {role}\nExperience: {years_of_experience} year\nLanguage: {fav_prog_lang}\n
""")
print(f"Future goal: \nBecome an AI Engineer")