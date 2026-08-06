###
# LARGEST PRIME FACTOR
###

import math

# fucntion that finds the smallest prime of the given number
def smallestPrime(number):
    assert number >= 2
    for factor in range(2, math.isqrt(number) + 1):
        if number % factor == 0:
            return factor
    return number

# main funciton that devides the goal number with the smallest
# prime untill the given prime is the same as the current goal
# and then returns it
def main():
    goal = 600851475143
    while True:
        prime = smallestPrime(goal)
        if prime < goal:
            goal //= prime
        else:
            return goal

if __name__ == '__main__':
    print(main())