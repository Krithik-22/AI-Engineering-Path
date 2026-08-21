# Q1
# Suppose:
# calculator.py
# contains:
# def add(a, b):
#     return a + b
# And main.py contains:
# import calculator

# print(calculator.add(5, 3))

# What gets printed?

# And why can main.py access add()?

# Q2
# What's the difference between:
# import math
# and:
# from math import sqrt
# How would you call sqrt() in each case?

# Q3
# Why is this:
# if __name__ == "__main__":
# useful?
# Explain it in your own words rather than giving me a textbook definition.


# Q1: If we run main.py, then the output will be 8. It can access add because we have imported calculator
# Q2: import math -> imports all functions within math, and whenever I use any one of it I have to do math., but in from math import sqrt, I'm only importing sqrt I dont have to use math.
# Q3: if in case I have imported a module which has executable or print lines when I run the main.py file the imported mofdule program will as well run and the output will be shown.
# Q4: Hello from calculator 5 because it executes those lines as well as __main__ is not used

# Q4 — Think carefully

# Suppose calculator.py contains:

# def add(a, b):
#     return a + b


# print("Hello from calculator")

# Then main.py contains:

# import calculator

# print(calculator.add(2, 3))

# What will the output be?

# And why does "Hello from calculator" execute even though we only imported the module?

# 💻 Coding Exercise 1

# Create two files:

# calculator.py
# main.py

# In calculator.py, create:

# add()
# subtract()
# multiply()
# divide()

# Then import those functions into main.py and use them.

# Handle division by zero appropriately.

# 💻 Coding Exercise 2

# Create:

# utils.py

# with:

# is_even(number)
# is_positive(number)

# Then import them into:

# main.py

# and test both functions.

# 🏆 Mini Challenge

# Create:

# math_utils.py

# with:

# square(number)
# cube(number)
# average(numbers)

# Then in main.py:

# Import the functions.
# Ask the user for numbers.
# Display the square/cube of a number.
# Calculate the average.
# ⭐ Bonus Challenge

# Use:

# if __name__ == "__main__":

# inside math_utils.py.

# For example:

# def square(number):
#     return number ** 2

# if __name__ == "__main__":
#     print(square(5))

# Then import math_utils from main.py.

# Observe what happens.

# This is an important experiment—I want you to actually run it, because seeing the difference between running and importing a module makes __name__ click much faster than memorizing the definition.