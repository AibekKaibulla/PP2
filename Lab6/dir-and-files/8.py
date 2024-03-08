import os
# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.

example_path = r"C:\Users\z1n3x\OneDrive\Desktop\pp2\hello.txt"

# Checking if the file exists
if os.path.exists(example_path):
    # Checking if the file is writable (and thus, is deletable)
    if os.access(example_path, os.W_OK):
        try:
            # Attempt to delete file
            os.remove(example_path)
        except Exception as e:
            # If the file couldn't have been deleted
            print(f"Error occured")
    else:
        print("Permission denied")
else:
    print("The file does not exist")