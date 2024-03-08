# Write a Python program to count the number of lines in a text file.

with open("sample.txt", "r") as f:
    number_of_lines = len(f.readline())

print(number_of_lines)