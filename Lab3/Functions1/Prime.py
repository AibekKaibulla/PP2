def filter_prime(input_list):
    primes = []
    for num in input_list:
        div_count = 0
        if num == 2:
            primes.append(num)
            continue
        elif num == 1:
            continue
        for divisor in range(2, num):
            if num % divisor == 0:
                div_count += 1
        if div_count == 0:
            primes.append(num)
    return primes

input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

print(filter_prime(input_list))
