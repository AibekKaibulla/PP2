import re

def find_sequences(text):
    # Write a Python program to replace all occurrences of space, comma, or dot with a colon
    pattern = '[ ,.]'

    replaced_text = re.sub(pattern, ':', text)

    return replaced_text

test_cases = [
    "as a,d,s/b",
    "ajdas i.da.!38...91.23.b",
    "adsadasD"
]

for test in test_cases:
    print(f"Test case: {test}\nReplaced: {find_sequences(test)}\n")