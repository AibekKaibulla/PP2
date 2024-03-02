import re

def split_at_uppercase(text):
    # Write a Python program to split a string at uppercase letters.
    pattern = '[A-Z][^A-Z]*'

    return re.findall(pattern, text)

test_string = "ThisIsString"

split_string = split_at_uppercase(test_string)

print(split_string)