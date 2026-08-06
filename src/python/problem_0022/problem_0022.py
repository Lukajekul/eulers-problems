###
# NAMES SCORES
###

# The goal is to find the names alphabetic valuse (summing up all the positions
# of the names letters in the alphabet) and multiplying it by its potional value
# in the ordered list.

alphabet = "abcdefghijklmnopqrstuvwxyz"

# Function calculates the alphabetic value of the name

def alphabeticValue(name):
    value = 0
    for letter in name:
        value += alphabet.index(letter) + 1
    return value

# Main function opens and read the .txt file and then itterates though the list
# of names and calculates all the values. The total value of all the names gets 
# printed at the end.

def main():
    nameValueList = []
    with open("names.txt") as file:
        names = file.read().replace('"', '').lower()
    namesList = names.split(",")
    namesList.sort()

    for name in range(len(namesList)):
        nameValueList.append((name + 1) * alphabeticValue(namesList[name]))

    return sum(nameValueList)


if __name__ == '__main__':
    print(main())