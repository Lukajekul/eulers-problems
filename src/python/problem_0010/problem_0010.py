###
# SUMMATION OF PRIMES
###

import math

sumPriume = 0

# Funciton checks if the number is prime or not and returns boolean value.

def is_prime(number):
    for i in range(2,math.isqrt(number)+1):
        if number % i == 0:
            return False
    return True

# Goes though 2 million itterations and summs up all the primes.

for number in range(2,2000001):
    if is_prime(number):
        sumPriume += number
print(sumPriume)