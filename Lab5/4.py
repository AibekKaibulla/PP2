import re

def find_sequences(text):
    # Write a Python program to find the sequences of one upper case letter followed by lower case letters.
    pattern = '[A-Z][a-z]*'
    
    matches = re.findall(pattern, text)

    return matches

test_case = "This is some Sample text with MixedCase Letters."

matches = find_sequences(test_case)
print(f"Test case: {test_case}\nMatches: {matches}\n")
