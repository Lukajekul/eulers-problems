longestSequence = 0
numberOfTheSequence = 0

for index in range(2, 1000001):
    sequence = 0
    collatzNumber = index
    while True:
        if collatzNumber == 1:
            if longestSequence < sequence:
                longestSequence = sequence
                numberOfTheSequence = index
            break
        if collatzNumber % 2 == 0:
            collatzNumber //= 2
            sequence += 1
        else:
            collatzNumber = (collatzNumber * 3) + 1
            sequence += 1
print(numberOfTheSequence)