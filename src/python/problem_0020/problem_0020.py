###
# FACTORIAL DIGIT SUM
###

# Uses the variable to store the factorial values
# in a reverse order from 100 to 1 to immitate fatorial
# and then itterates through its string form to intpu
# each int into a list that gets summed at the end.

sumNumber = 1
sumList = []
for number in range(100,0,-1):
    sumNumber *= number
for number in str(sumNumber):
    sumList.append(int(number))
print(sum(sumList))