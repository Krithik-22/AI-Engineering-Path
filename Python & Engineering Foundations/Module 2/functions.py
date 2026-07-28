# Question 1
# def hello():
#     print("Hello")

# hello()

# Why doesn't "Hello" print until we call hello()?

# Q1: Because the print statement of hello is within the function hello() and will not execute that line until the function is called
# Q2: Because the function greet is called with the argument Python
# Q3: It would thrown an error because message is a variable within the scope of that function and it cannot be called outside

# Question 2
# def greet(name):
#     print(name)

# greet("Python")

# Why is "Python" printed?

# Question 3
# def demo():
#     message = "Hi"

# demo()

# print(message)

# Why does this produce an error?

# 💻 Coding Exercise 1

# Write a function called:

# say_hello()

# It should print:

# Hello, AI Engineer!

# Then call the function.

def say_hello():
    print("Hello, AI Engineer!")

say_hello()

# 💻 Coding Exercise 2

# Write a function:

# square(number)

# It should print the square of the given number.

# Example:

# square(5)

# Output

# 25

def square(num):
    print(num ** 2)

square(5)
# 🏆 Mini Challenge

# Create a function:

# student_report(name, marks)

# Output example:

# Student: Krithik
# Marks: 95
# Result: Pass

# If marks are below 35, print:

# Result: Fail

# Use an if statement inside the function.

def student_report(name, marks):
    result = "Pass" if marks >= 35 else "Fail"

    print(f"""
    Student: {name}
    Marks: {marks}
    Result: {result}
    """)
student_report("Krithik",47)

# ⭐ Bonus Challenge

# Create a function:

# calculator(a, b)

# Print:

# Sum
# Difference
# Product
# Division

# For example:

# calculator(20, 5)

# Output:

# Sum: 25
# Difference: 15
# Product: 100
# Division: 4.0

def calculator(a,b):
    division = None
    if b != 0:
        division = a / b
    else:
        division = -1
    print(f"""
    Sum : {a + b}
    Difference: {a - b}
    Product: {a * b}
    Division: {division}
    """)

calculator(10,0)

# Question 1
# def hello():
#     print("Hello")

# value = hello()

# Why is value equal to None?

# Q1: By default a function return None
# Q2: because the function hello() returns string "hello", it is stored in variable value and when prints ValueError
# Q3: the add method returns the sum of a and b, when we print the method it prints the value returned from the function

# Question 2
# def hello():
#     return "Hello"

# value = hello()

# print(value)

# Why does this print

# Hello

# instead of

# None
# Question 3
# def add(a,b):

#     return a+b

# print(add(5,3))

# Where does the value

# 8

# come from?

# Explain the execution.

# 💻 Coding Exercise 1

# Rewrite this function using return.

# def cube(number):

#     print(number**3)

# Use it like this:

# answer = cube(4)

# print(answer)

# Expected Output

# 64

def cube(number):
    return number ** 3

# 💻 Coding Exercise 2

# Create

# def rectangle_area(length,width):

# Return

# length * width

# Then

# area = rectangle_area(10,5)

# print(area)

# Output

# 50

def rectangle_area(length, width):
    return length * width


# 🏆 Mini Challenge

# Create

# def student_result(name,marks):

# Return

# "{name} passed"

# or

# "{name} failed"

# depending on marks.

# Example

# print(student_result("Krithik",91))

# Output

# Krithik passed

def student_result(name, marks):
    result = "passed" if marks >= 35 else "failed"

    return f"{name} {result}"
# ⭐ Bonus Challenge

# Create

# def calculator(a,b):

# Return four values:

# Sum
# Difference
# Product
# Division

# Example:

# s,d,p,div = calculator(20,5)

# print(s)
# print(d)
# print(p)
# print(div)

# Expected Output

# 25
# 15
# 100
# 4.0

def calculator(a, b):
    if b != 0:
        return a+b, a-b, a*b, a/b
    return a+b, a-b, a*b, "cannot divide by zero"