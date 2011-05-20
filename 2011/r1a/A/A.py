import sys
from math import ceil

# the function to calculate the GCD
def gcd(num1, num2):
    result = 1
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result

# the function to calculate the LCM
def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result


def main():
    #sys.stdin = open("test.in")
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N, PD, PG = map(int, sys.stdin.readline().split(" "))
        print ""
        print N, PD, PG
        lcm1 = lcm(PD, 100)
        lcm2 = lcm(PG, 100)
        if PD != 0:
            d = lcm1 / PD
            wd = lcm1 / 100
        if PG != 0:
            g = lcm2 / PG
            w = lcm2 / 100
        if (PD == 0 and PG == 0) or (PD == 0 and PG !=0):
            print "Case #%d: %s" % (t, 'Possible')
            continue
        elif PD !=0 and PG == 0:
            print "Case #%d: %s" % (t, 'Broken')
            continue
        
        if PD >= PG:
            scale = int(ceil(float(wd)/w))
        else:
            if g-w != 0:
                scale = int(ceil(float(d-wd)/(g-w)))
            else:
                scale = 0
        w *= scale
        g *= scale
        print d, wd, d-wd
        print g, w, g-w
        if d > N or g < d:
            print "Case #%d: %s" % (t, 'Broken')
        else:
            print "Case #%d: %s" % (t, 'Possible')
            
if __name__ == '__main__':
    main()
