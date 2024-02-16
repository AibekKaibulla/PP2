def even(n):
    
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


gen = even(int(input()))

for x in gen:
    print(x, end=', ')
    
print()