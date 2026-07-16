import math

goal = 600851475143

primefactors = []

def isPrime(number):
    otherFactors = []
    for factor in range(1,math.floor(math.sqrt(number))):
        if number % factor == 0:
            otherFactors.append(factor)
    if len(otherFactors) == 0:
        return True

for factor in range(1, goal, 2):
    if goal % factor == 0:
        if isPrime(factor):
            primefactors.append(factor)

print(primefactors[-1])