import math

def is_prime(number):
    for i in range(2,math.isqrt(number)+1):
        if number % i == 0:
            return False
    return True

placeHolder = 0
currentNuber = 1
while placeHolder < 10001:
    currentNuber += 1
    if is_prime(currentNuber):
        placeHolder +=1
print(currentNuber)