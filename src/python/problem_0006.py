sumInt = []
squere = 0
for intiger in range(101):
    sumInt.append(intiger)
    squere += intiger**2
print((sum(sumInt)**2) - squere)