# 🏋️ Mini Exercise

# Write a program called Student Score Analyzer.

# Requirements:

# Create a list of 5 marks (hardcode them for now, for example [78, 92, 85, 67, 90]).
# Print:
# Total marks
# Highest mark
# Lowest mark
# Average mark (rounded to 2 decimal places)
# Marks sorted in ascending order
# Marks sorted in descending order

# Use:

# sum()
# max()
# min()
# len()
# round()
# sorted()

marks = [78, 92, 85, 67, 90]

print(f"""
# Total marks                               :{sum(marks)}
# Highest mark                              :{max(marks)}
# Lowest mark                               :{min(marks)}
# Average mark (rounded to 2 decimal places):{round(sum(marks)/len(marks),2)}
# Marks sorted in ascending order           :{sorted(marks)}
# Marks sorted in descending order          :{sorted(marks,reverse=True)}
""")


# 1️⃣ enumerate()
# Instead of:

# fruits = ["Apple", "Banana", "Orange"]

# for i in range(len(fruits)):
#     print(i, fruits[i])

# Pythonic way:
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# Output:
# 0 Apple
# 1 Banana
# 2 Orange

# Much cleaner.

# 2️⃣ zip()

# Suppose you have:

# names = ["Krithik", "Rahul", "Arjun"]
# scores = [95, 87, 91]

# Instead of manually matching them:

# for name, score in zip(names, scores):
#     print(name, score)

# Output:

# Krithik 95
# Rahul 87
# Arjun 91

# You'll use zip() when combining related data from different sources.

# 3️⃣ any()

# Checks if at least one value is True.

# results = [False, False, True]

# print(any(results))

# Output:

# True

# This is useful when checking conditions like "Did any API request fail?" or "Did any document match the search?"

# 4️⃣ all()

# Checks if every value is True.

# results = [True, True, True]

# print(all(results))

# Output:
# True



