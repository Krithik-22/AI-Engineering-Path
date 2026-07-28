# Q1
# square = lambda x: x * x

# print(square(6))

# Why is the output 36?

# Q1: because sqaue stores the lambda function and when it is called with the argument 6 it returns the logic written there
# Q2: for each number in the numbers list the lambda function is executed for map method
# Q3: for eac number in the numbers list the lambda function is executed for the filter and as the function only returns for numbers grater than 10

# Q2
# numbers = [1, 2, 3]

# result = list(map(lambda x: x + 10, numbers))

# print(result)

# Why is the output:

# [11, 12, 13]
# Q3
# numbers = [5, 10, 15, 20]

# result = list(filter(lambda x: x > 10, numbers))

# print(result)

# Why does the output contain only 15 and 20?

# 💻 Coding Exercise 1

# Create a lambda function that returns the cube of a number.

# Example:

# cube = lambda x: ...
# print(cube(3))

# Expected output:

# 27

cube = lambda x : x ** 3

# 💻 Coding Exercise 2

# Given:

# numbers = [2, 4, 6, 8]

# Use map() and a lambda to create a new list where each number is doubled.

# Expected output:

# [4, 8, 12, 16]

numbers = [2, 4, 6, 8]
doubled_numbers = list(map(lambda x : x * 2, numbers))

# 🏆 Mini Challenge

# Given:

students = [
    ("Krithik", 91),
    ("Alice", 85),
    ("Bob", 95),
    ("Charlie", 78)
]

# Sort the list by marks in descending order using a lambda.

sorted_list = students.sort(key = lambda student : student[1], reverse=True)

# ⭐ Bonus Challenge

# Given:

employees = [
    {"name": "Krithik", "salary": 70000},
    {"name": "Rahul", "salary": 50000},
    {"name": "Alice", "salary": 90000}
]

# Use:

# sorted()

# with a lambda to sort employees by salary from highest to lowest.

sorted_employee_list = employees.sort(key = lambda employee : employee["salary"], reverse=True)