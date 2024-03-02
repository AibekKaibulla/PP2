# Write a Python program to insert spaces between words starting with capital letters.
import re

def insert_spaces(text):
    pattern = r'(?<=[a-z])(?=[A-Z])'
    
    return re.sub(pattern, ' ', text)

test_string = "ThisIsString"

result_string = insert_spaces(test_string)

print(result_string)