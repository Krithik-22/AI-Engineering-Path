# Question 1
# count = 1

# while count <= 3:
#     print(count)
#     count += 1

# Why does this loop stop?

# Question 2
# count = 1

# while count <= 3:
#     print(count)

# Why is this an infinite loop?

# Question 3
# password = ""

# while password != "python":
#     password = input("Password: ")

# Why is while a better choice than for here?

# 💻 Coding Exercise 1

# Print numbers 1 to 10 using a while loop.

count = 1

while count <= 10:
    print(count)
    count += 1

# 💻 Coding Exercise 2

# Ask the user to enter a positive number.

# If they enter a negative number, ask again.

# Keep asking until the number is positive.

# Then print:

# Valid number entered!

num = -1

while num < 0:
    num = int(input("Enter a positive number: "))
print("Valid number entered")

# 🏆 Mini Challenge

# Build a simple PIN Verification System.

# Correct PIN:

# 4321

# Requirements:

# Ask the user to enter the PIN.
# If incorrect, ask again.
# Keep asking until the correct PIN is entered.
# Then print:
# Access Granted

attempts = 0
correct_pin = 4321
pin = 0

while pin != correct_pin and attempts < 3:
    pin = int(input("Enter the PIN: "))
    attempts += 1
if attempts >= 3 and pin != correct_pin:
    print("Account Locked")
else:
    print("Access Granted")

# ⭐ Bonus Challenge

# Improve the PIN system:

# User gets only 3 attempts.
# If they fail all 3:
# Account Locked

# Hint:

# You'll need two variables:

# attempts = 0
# correct_pin = "4321"

# Think about how attempts should change each time through the loop.

# 🧠 New Thinking Habit

# Whenever you see a while loop, ask yourself these two questions:

# 1.

# What changes inside the loop?

# If the answer is nothing...

# 🚨 You're probably creating an infinite loop.

# 2.

# What eventually makes the condition become False?

# If you can't answer that...

# The loop may never stop.

# Professional developers mentally ask these questions every time they write a while loop.


# Q1: on every iteration the count value increases once it changes to 4 the condition becomes false and exits
# Q2: The count variable is not changing at all for the condition to get false at some point, hence it becomes an infinite loop
# Q3: If used for the user can have only limited number of attempts, since it is a while the user can attempt as long as he gets the password correct

# while ... else

# Most Python beginners don't know this exists.

# Python allows:

# while condition:
#     print("Running")
# else:
#     print("Loop finished normally")

# The else block runs only if the loop ends naturally (i.e., the condition becomes False).

# If the loop is terminated with break, the else block is skipped.