###
# SUM SQUERE DIFFERANCE
###

# This problem takes squere of sums and sutracts the sum of squeres
# from it. Uses one for loop that itterates to 100 and then appends
# the nuber to a list and adds its squere to the variable. At the end
# calculates the differance.

sumInt = []
squere = 0
for intiger in range(101):
    sumInt.append(intiger)
    squere += intiger**2
print((sum(sumInt)**2) - squere)