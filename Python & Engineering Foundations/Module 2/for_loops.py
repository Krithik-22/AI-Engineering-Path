# Question 1
# for number in range(1, 6):
#     print(number)

# Why is 6 not printed?

# Question 2
# for letter in "AI":
#     print(letter)

# Why does the loop run exactly twice?

# Question 3
# languages = ["Python", "Java", "Go"]

# for language in languages:
#     print(language)

# What is stored in the variable language during each iteration?

# 💻 Coding Exercise 1

# Print the numbers 1 to 20.

# Requirements:

# Use a for loop.
# Print only the even numbers.

for number in range(1, 20):
    if number % 2 == 0:
        print(number)

for num in range(2, 20, 2):
    print(num)

# 💻 Coding Exercise 2

# Ask the user to enter a word.

# Print each character on a new line.

# Example:

# Input:
# Python

# Output:

# P
# y
# t
# h
# o
# n

word = input("Enter any word: ")

for letter in word:
    print(letter)

# 🏆 Mini Challenge

# Build a Student Marks Analyzer.

# marks = [85, 91, 76, 98, 67]

# Using a for loop:

# Print every mark.
# Print "Pass" if the mark is 35 or above, otherwise "Fail".

# Expected output:

# 85 -> Pass
# 91 -> Pass
# 76 -> Pass
# 98 -> Pass
# 67 -> Pass

# If you change one mark to 20, your program should print:

# 20 -> Fail

marks = [85, 91, 76, 98, 67]
total = 0
for mark in marks:
    total += mark
    if mark >= 35:
        print(f"{mark} -> Pass")
    else:
        print(f"{mark} -> Fail")
print(total)


# ⭐ Bonus Challenge (Optional)

# Using:

# marks = [85, 91, 76, 98, 67]

# Calculate the total without using sum().


