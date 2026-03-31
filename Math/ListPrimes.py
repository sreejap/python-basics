def list_primes(n):
    if n < 2:
        return []
    
    primes = []
    
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    
    return primes


# Take input from user
n = int(input("Enter a number: "))

# Get and print primes
primes = list_primes(n)
print("Prime numbers from 1 to", n, "are:")
print(primes)
