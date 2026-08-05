###
# LARGEST PALINDROME PRODUCT 
###

# goes though two loops from 100 to 999 (included) since it is looking only 3 digit numbers
# adds them together and checks if the product is a palindrome and if the palindrome is lager
# then the previus one. A palindrome is a number that reads the same both ways.

largestPalindrome = 0

for productOne in reversed(range(100,1000)):
    for productTwo in reversed(range(100,1000)):
        if str(productOne * productTwo) == str(productOne * productTwo)[::-1] and (productOne * productTwo) > largestPalindrome:
            largestPalindrome = productOne * productTwo
print(largestPalindrome)