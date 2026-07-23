# Write a program called Text Analyzer.

# Requirements:

# Ask the user for a sentence.
# Print:
# Original sentence
# Uppercase
# Lowercase
# Number of characters
# Number of words
# Check whether the sentence starts with "AI" (case-sensitive for now).
# Replace every occurrence of "AI" with "Artificial Intelligence".
# Print the cleaned sentence.

# Example:

# Enter a sentence:
# AI is amazing

# Output:

# Original : AI is amazing
# Upper    : AI IS AMAZING
# Lower    : ai is amazing
# Characters : 13
# Words      : 3
# Starts with AI : True
# Updated : Artificial Intelligence is amazing

sentence = input("Enter a sentence: ")

print(f"""
original    :   {sentence}
Upper       :   {sentence.upper()}
Lower       :   {sentence.lower()}
Characters  :   {len(sentence)}
Words       :   {len(sentence.split())}
Starts with AI: {sentence.startswith("AI")}
Updated:    :   {sentence.replace("AI", "Artificial Intelligence")}
""")