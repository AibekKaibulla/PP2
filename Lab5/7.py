import re

def snake_to_camel(text):
    # Write a python program to convert snake case string to camel case string.
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text)

test_cases = [
    "this_is_a_snake_case_string",
    "example_variable_name",
    "snake_case_to_camel_case"
]

for test in test_cases:
    camel_case = snake_to_camel(test)
    print(f"Snake_case: {test}\nCamel_case: {snake_to_camel(test)}\n")