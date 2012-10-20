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
        #print ""
        #print N, PD, PG
        possible = "Case #%d: Possible"
        broken = "Case #%d: Broken"
        if (PD == 0 and PG == 0) or (PD == 0 and PG !=0 and PG != 100):
            print possible % t
            continue
        elif PD !=0 and PG == 0:
            print broken % t
            continue
        elif PG == 100 and PD != 100:
            print broken % t
            continue
        lcm1 = lcm(PD, 100)
        d = lcm1 / PD
        wd = lcm1 / 100
        #print d, wd
        if d > N:
            print broken % t
        else:
            print possible % t
            
if __name__ == '__main__':
    main()
