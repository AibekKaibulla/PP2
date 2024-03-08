import os

# Write a Python program to test whether a given path exists or not.
# If the path exist find the filename and directory portion of the given path.

example_path = r"C:\Users\z1n3x\OneDrive\Desktop\pp2"

if os.path.exists(example_path):
    print("Path exists.")
    print("Contents", os.listdir(example_path))

    directory, filename = os.path.split(example_path)

    print("Directory portion: ", directory)
    print("Filename portion: ", filename)
else:
    print("Path does not exist.")
