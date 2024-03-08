# Write a Python program to copy the contents of a file to another file

r = open("hello.txt", "r")
h = open("hello1.txt", "w")

h.write(f"{r.read()}")
h.close()
r.close()

# This code works only if the source file exists