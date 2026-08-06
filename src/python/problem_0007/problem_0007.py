###
# 10 001ST PRIME
###

import math

# Function checking if the number is prime and returning a 
# boolean value accorting to if the number is or isnt
# a prime.

def is_prime(number):
    for i in range(2,math.isqrt(number)+1):
        if number % i == 0:
            return False
    return True

# While loop that itterates to 10001 times of which a prime accurs
# and at the end prints the current prime

placeHolder = 0
currentNuber = 1
while placeHolder < 10001:
    currentNuber += 1
    if is_prime(currentNuber):
        placeHolder +=1
print(currentNuber)