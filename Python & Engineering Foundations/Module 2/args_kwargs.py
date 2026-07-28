# Question 1
# def demo(*args):
#     print(args)

# demo(10,20,30)

# Why is the output a tuple?

# Q1: the positional arguments gets stored with type tuple in the same order
# Q2: the keyword arguments gets stored in the type of dictionary so we have a kev value PendingDeprecationWarning
# Q3: because * values gets stored as a tuple which can be iterated over

# Question 2
# def demo(**kwargs):
#     print(kwargs)

# demo(name="Krithik", age=23)

# Why is the output a dictionary?

# Question 3
# def demo(*values):

#     for value in values:
#         print(value)

# Why can we use a for loop on values?

# 💻 Coding Exercise 1

# Create

# def average(*numbers):

# Return the average of all numbers.

# Example

# print(average(10,20,30))

# Output

# 20.0

def average(*numbers):
    sum = 0;

    for num in numbers:
        sum += num

    return sum/len(numbers)


# 💻 Coding Exercise 2

# Create

# def profile(**details):

# Print

# name : Krithik
# role : AI Engineer
# city : Chennai

# Use a loop over the dictionary.

def profile(**details):
    for key, value in details.items():
        print(f"{key}   :   {value}")

# 🏆 Mini Challenge

# Create

# def shopping_cart(*prices):

# Return

# Total price
# Highest price
# Lowest price

# Example

# total, high, low = shopping_cart(100,250,75,400)

# Output

# 825
# 400
# 75

def shopping_cart(*prices):
    return sum(prices), max(prices), min(prices)


# ⭐ Bonus Challenge

# Create a function:

# def employee(*skills, **details):

# Example call:

# employee(
#     "Python",
#     "SQL",
#     "Docker",
#     name="Krithik",
#     company="Kaleris",
#     role="Support Engineer"
# )

# Output:

# Skills
# ------
# Python
# SQL
# Docker

# Details
# -------
# name : Krithik
# company : Kaleris
# role : Support Engineer

# This combines both *args and **kwargs—a pattern you'll encounter in real Python libraries.

def employee(*skills, **details):
    print("Skills")
    print("--------")

    for skill in skills:
        print(skill)

    print("Skills")
    print("--------")

    for key, value in details.items():
        print(f"{key} : {value}")


# Q1: the positional arguments gets stored with type tuple in the same order
# Q2: the keyword arguments gets stored in the type of dictionary so we have a kev value PendingDeprecationWarning
# Q3: because * values gets stored as a tuple which can be iterated over
