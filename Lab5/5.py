import re

def find_sequences(text):
    # Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
    pattern = 'a.*b'

    matches = re.findall(pattern, text)

    return matches

test_cases = [
    "asadsb",
    "ajdasida!389123.b",
    "adsadasD"
]

for test in test_cases:
    print(f"Test case: {test}\nMatches: {find_sequences(test)}\n")