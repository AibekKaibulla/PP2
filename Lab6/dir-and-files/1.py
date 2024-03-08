import os

# Write a Python program to list only directories, 
# files and all directories, files in a specified path.

example_path = r"C:\Users\z1n3x\OneDrive\Desktop\pp2"
entries = os.listdir(example_path)

directories = []
files = []

for entry in entries:
    full_path = os.path.join(example_path, entry)
    if os.path.isdir(full_path):
        directories.append(entry)
    elif os.path.isfile(full_path):
        files.append(entry)

print("Directories:")
for directory in directories:
    print(directory)

print("\nFiles:")
for file in files:
    print(file)

print("\nAll Directories and Files:")
for entry in entries:
    print(entry)