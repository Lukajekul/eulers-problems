import math

cycle = 1
triangleNumber = 0


def factorCheck(triNum):
    root = math.isqrt(triNum)
    koeficients = 0
    for num in range(1, root + 1):
        if triNum % num == 0:
            koeficients += 2
    if root * root == triNum: 
        koeficients -= 1
    return koeficients

while True:
    triangleNumber += cycle
    if factorCheck(triangleNumber) > 500:
        print(triangleNumber)
        break
    cycle += 1
