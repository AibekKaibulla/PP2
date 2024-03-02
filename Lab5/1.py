import re

def find_sequences(text):
    # Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
    pattern = 'ab*'

    matches = re.search(pattern, text)

    return matches is not None

test_cases = [
    "abbbbb",
    "a",       
    "ab",      
    "abnormal",
    "abb",     
    "abbb",    
]

for test in test_cases:
    print(f"Test case: {test}\n Matches: {find_sequences(test)}\n")