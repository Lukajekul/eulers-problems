###
# AMICABLE NUMBERS
###

# The goal is to find all the amicable numbers (numbers where the sum of divisors
# of that number if we again sum the divisors of that new number match the initial
# number).

amicableNumbers = []

# Fuction that takes a number and itterates up to it in a for loop checks for
# its devisors and adds them together.

def sumDivisors(number):
    sumList = []
    for divisor in range(1, (number//2) + 1):
        if number % divisor == 0:
            sumList.append(divisor)
    return sum(sumList)

# Fucniton takes a possible amicable number, sets 2 variables the input one and
# its divisors sum and compares the input to again devisor sumed number that was
# summed before. Also checks that the numbers arent the same.

def isAmicable(amicableContender):
    number1 = amicableContender
    number2 = sumDivisors(amicableContender)
    if number1 != number2 and number1 == sumDivisors(number2):
        return True

# loops up to 10000 and checks if the number is a amicable number, if is
# add is to a list that gets summed at the end print.

for number in range(10001):
    if isAmicable(number):
        amicableNumbers.append(number)
print(sum(amicableNumbers))