largestPalindrome = 0

for productOne in reversed(range(100,1000)):
    for productTwo in reversed(range(100,1000)):
        if str(productOne * productTwo) == str(productOne * productTwo)[::-1] and (productOne * productTwo) > largestPalindrome:
            largestPalindrome = productOne * productTwo
print(largestPalindrome)