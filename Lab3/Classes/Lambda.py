class filter_prime:

    def isPrime(self, num):
        if (num < 2):
            return False
        else:
            for i in range(2, num):
                if (num % i == 0):
                    return False
        return True
    
    def filter_primes(self, list_prime):
        return filter(lambda x : self.isPrime(x), list_prime)
    
prime = filter_prime()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
prime_numbers = list(prime.filter_primes(nums))
print(prime_numbers)