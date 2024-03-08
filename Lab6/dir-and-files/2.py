import os

# Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path

example_path = r"C:\Users\z1n3x\OneDrive\Desktop\pp2"

exists = os.path.exists(example_path)
print(f"Exists: {exists}")

readable = os.access(example_path, os.R_OK)
print(f"Readable: {readable}")

writable = os.access(example_path, os.W_OK)
print(f"Writable: {writable}")

executable = os.access(example_path, os.X_OK)
print(f"Executable: {executable}")