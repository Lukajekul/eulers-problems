###
# EVEN FIBONACCI NUMBERS
###

# uses two variables to hold both of the currently in use numbers of the sequence
# and two lists one to fill with the sequence and one to collect all the even values

# list that holds all the values of the sequence
sequence = [1]

# list that holds all the even numbers of the sequence
values = []

# both last number place holders
firstPlaceHolder = 1
secondPlaceHolder = 2

# while loop iterates till the sencond placeholder is less the 400 000 since
# then the first one will be 600 000 so the next iterations would already pass
# the million mark. Then checks if the number is even adds it into the list,
# updates both placeholders and at the end prints the sum.
while secondPlaceHolder < 4000000:
    if secondPlaceHolder % 2 == 0:
        values.append(secondPlaceHolder)
    sequence.append(secondPlaceHolder)
    secondPlaceHolder += firstPlaceHolder
    firstPlaceHolder = sequence[-1]
print(sum(values))