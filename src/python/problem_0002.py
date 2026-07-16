sequence = [1]
values = []
firstPlaceHolder = 1
secondPlaceHolder = 2
while secondPlaceHolder < 4000000:
    if secondPlaceHolder % 2 == 0:
        values.append(secondPlaceHolder)
    sequence.append(secondPlaceHolder)
    secondPlaceHolder += firstPlaceHolder
    firstPlaceHolder = sequence[-1]
print(sum(values))