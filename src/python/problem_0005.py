# VERSION 1
import math
print(math.lcm(*range(1,21)))

# VERISON 2
def smallestProduct():
    number = 20
    while True:
        remainders = [True]
        for factor in range(1,21):
            if number % factor != 0:
                remainders.append(False)
        if all(remainders):
            return(number)
        number += 1

if __name__ == '__main__':
    print(smallestProduct())