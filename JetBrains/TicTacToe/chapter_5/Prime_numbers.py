prime_numbers = []

for possiblePrime in range(2, 1001):
    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, possiblePrime):
        if possiblePrime % num == 0:
            isPrime = False
    if isPrime:
        prime_numbers.append(possiblePrime)

print(prime_numbers)


# =========================================================================
# solutions

prime_numbers = [x for x in range(2, 1000) if all(x % n for n in range(2, x))]
print(prime_numbers)
# =========================================================================
# prime_numbers = [x for x in range(2, 1000) if all(x % y != 0 for y in range(2, x))]

# =========================================================================
odd_numbers = range(3, 1000, 2)
# prime_numbers = [2] + [num for num in odd_numbers if all(num % divisor for divisor in range(2, num))]


