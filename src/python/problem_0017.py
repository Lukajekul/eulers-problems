singels = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen","seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = "hundred"
addIn = "and"
thousand = "thousand"

fullCount = ""

for toTen in range(9):
    fullCount += singels[toTen]
for teen in range(10):
    fullCount += teens[teen]
for ten in range(8):
    fullCount += f"{tens[ten]}"
    for toTen in range(9):
        fullCount += f"{tens[ten]} {singels[toTen]}"
for hundred in range(9):
    fullCount += f"{singels[hundred]} {hundreds}"
    for toTen in range(9):
        fullCount += f"{singels[hundred]} {hundreds} and {singels[toTen]}"
    for teen in range(10):
        fullCount += f"{singels[hundred]} {hundreds} and {teens[teen]}"
    for ten in range(8):
        fullCount += f"{singels[hundred]} {hundreds} and {tens[ten]}"
        for toTens in range(9):
            fullCount += f"{singels[hundred]} {hundreds} and {tens[ten]} {singels[toTens]}"
fullCount += f"{singels[0]} {thousand}"

countSentence = fullCount.replace(" ", "")
print(len(countSentence))