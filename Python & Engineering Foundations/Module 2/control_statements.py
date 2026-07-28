# Question 1
# for number in range(1, 6):
#     if number == 4:
#         break

#     print(number)

# Why are only 1, 2, and 3 printed?

# Q1: Because once break is executed after the if condition becomes true, the loop breaks.
# Q2: This skips all the even numbers because the if condition checks if it divisible by 2 and skips that iteration
# Q3: When I have not planned to write it yet but I just need the function to use as a placeholder somehwere else, I might need the definition

# Question 2
# for number in range(1, 6):
#     if number % 2 == 0:
#         continue

#     print(number)

# Why are only odd numbers printed?

# Question 3
# def process_data():
#     pass

# Why would a programmer intentionally leave a function empty?

# 💻 Coding Exercise 1

# Print numbers from 1 to 10.

# Skip multiples of 3 using continue.

# Expected output:

# 1
# 2
# 4
# 5
# 7
# 8
# 10

for num in range(1,11):
    if num % 3 == 0:
        continue
    print(num)


# 💻 Coding Exercise 2

# Ask the user to enter numbers continuously.

# If they enter:

# 0

# stop the loop.

# Otherwise print:

# You entered: X

# Use break.

num = None

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break

    print(f"You entered: {num}")

# 🏆 Mini Challenge

# Create a simple Guess the Secret Number game.

# Secret number:

# 7

# Rules:

# Keep asking the user to guess.
# If the guess is wrong:
# Try Again
# If the guess is correct:
# Correct!

# Then exit the loop using break.

secret_number = 7

while True:
    num = int(input("Guess the Secret Number: "))

    if num == secret_number:
        print("Correct!")
        break

    print("Try Again")

# ⭐ Bonus Challenge

# Create a menu:

# 1. Say Hello
# 2. Say Bye
# 3. Exit

# The program should keep showing the menu until the user chooses 3.

# Hint:

# while True:

# You'll use:

# while
# if
# break

# This is how many command-line applications are structured.


while True:
    print("""
        1. Say Hello
        2. Say Bye
        3. Exit
    """)
    choice = int(input("What is your choice: "))

    if choice == 3:
        break

