import re

def find_sequences(text):
    # Write a Python program to find sequences of lowercase letters joined with a underscore.
    pattern = '[a-z]+_[a-z]+'

    matches = re.findall(pattern, text)

    return matches

test_cases = [
    "example_test_case",
    "anotherExample_test_case_again",
    "no_match_here",
    "multiple_matches_in_this_example_test_case"
]

for test in test_cases:
    print(f"Test Case: {test}\nMatches: {find_sequences(test)}\n")