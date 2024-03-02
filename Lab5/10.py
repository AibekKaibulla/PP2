import re

def camel_to_snake(camel_str):
    # Write a Python program to convert a given camel case string to snake case.
    snake_str = re.sub(r'(?<=\w)([A-Z])', r'_\1', camel_str)

    return snake_str.lower()

test_cases = [
    "CamelCaseString",
    "ThisIsATestString",
    "CamelCaseToSnakeCase"
]

for test in test_cases:
    snake_case = camel_to_snake(test)
    print(f"Camel Case: {test}\nSnake Case: {snake_case}\n")
