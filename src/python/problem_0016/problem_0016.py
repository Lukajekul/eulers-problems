import math

num = math.pow(2,1000)

# FORMATING THE NUMBER SO IT ISNT STORED AS A "e+301"
number = f"{num:.0f}"

fullSum = 0

for i in number:
    fullSum += int(i)

print(fullSum)