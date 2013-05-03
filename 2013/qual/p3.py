from math import sqrt, floor, ceil

def isPalindrome(num):
    tmp = num
    digits = []
    while tmp > 0:
        digits.append(tmp % 10)
        tmp = tmp / 10

    l = len(digits)
    for i in range(0, int(ceil(l/2.0))):
        if digits[i] != digits[l-i-1]:
            return False
    return True


def runCase(a, b):
    upper = int(floor(sqrt(b)))
    lower = int(ceil(sqrt(a)))
    counter = 0
    for i in range(lower, upper+1):
        if isPalindrome(i):
            square = i * i
            if isPalindrome(square):
                counter = counter + 1
    return counter        


n = int(raw_input(""))
for i in range(1, n+1):
    tmp = raw_input("")
    a, b = map(int, tmp.split())
    result = runCase(a, b)

    print "Case #%d: %d" % (i, result) 
