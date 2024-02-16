def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

i_squares = squares(3, 6)

for square in i_squares:
    print(square)