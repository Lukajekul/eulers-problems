import math

sumPriume = 0

def is_prime(number):
    for i in range(2,math.isqrt(number)+1):
        if number % i == 0:
            return False
    return True

for number in range(2,2000001):
    if is_prime(number):
        sumPriume += number
print(sumPriume)