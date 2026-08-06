###
# SMALLEST MULTIPLE
###

# Looks for the smallest multiple of the numbers from 1 to 20.

# Version 1 uses a math fucniton that lcm (least common multiple)
# with the given range to find it.

# VERSION 1
import math
print(math.lcm(*range(1,21)))

# Version 2 uses the a while loop to test all the numbers from 20
# forward and checks if the number is divisible by the factor in the
# for loop. If it is not it appends False into the list and at the end
# of the for loop if the list is all true it ends the  loop and prints
# out the lcm value.

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