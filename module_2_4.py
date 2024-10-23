# Init
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False

# Code
for number in numbers:
    for delimiter in range(2, number):
        if number % delimiter == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if number == 2 or is_prime:
        primes.append(number)
    elif number != 1:
        not_primes.append(number)

# Result
print("Простые числа: ", primes)
print("Составные числа: ", not_primes)