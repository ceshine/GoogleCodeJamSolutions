from math import sqrt, floor, ceil, log

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

def createPalindrome(digits, current, level, length, lower, upper):
    counter = 0
    for i in range(0, 9):
        if current == 0 and i == 0:
            continue
        digits[current] = i
        digits[length - current - 1] = i

        if current == level:
            num = 0
            for j in range(0, length):
                num = num* 10 + digits[j]
            if num >= lower and num <= upper and isPalindrome(num*num):
                counter = counter + 1
        else:
            counter =  counter + createPalindrome(digits, current+1, level, length, lower, upper)
    return counter
                         

def runCase(a, b):
    upper = int(floor(sqrt(b)))
    lower = int(ceil(sqrt(a)))
    lower_base = int(floor(log(lower, 10)))+1
    upper_base = int(floor(log(upper, 10)))+1
    counter = 0
    for i in range(lower_base, upper_base+1):
        digits = [0 for j in range(0, i)]
        counter =  counter + createPalindrome(digits, 0, int(ceil(i/2.0))-1, i, lower, upper)
    return counter        


n = int(raw_input(""))
for i in range(1, n+1):
    tmp = raw_input("")
    a, b = map(int, tmp.split())
    result = runCase(a, b)

    print "Case #%d: %d" % (i, result) 
