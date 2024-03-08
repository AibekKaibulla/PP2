import json

# Write a Python program to write a list to a file.

example_list = ["asd", 1, True, {"number": 42}]

with open("sample.txt", "w") as f:
    json.dump(example_list, f)