# Write a Python program with builtin function that returns True if all elements of the tuple are true.

def true(tuple):
    return all(tuple)


tuple1 = (1, 1, 1)
tuple2 = (1, 1, 0)

print(true(tuple1))
print(true(tuple2))
