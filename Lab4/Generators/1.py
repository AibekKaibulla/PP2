def square(n):
    i = 1
    while i * i <= n:
        yield i * i
        i += 1

gen = square(256)

for x in gen:
    print(x)