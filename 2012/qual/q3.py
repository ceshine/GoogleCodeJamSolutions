def solve(A, B):
    power = 1
    tmp = A
    while(tmp >= 10):
        power *= 10
        tmp /= 10

    count = 0
    for i in range(A, B+1):
        tmp = i
        while(True):
            tmp = tmp / 10 + (tmp % 10) * power
            if tmp == i:
                break
            elif tmp > i and tmp <= B:
                count += 1
    return count


n = int(raw_input(""))

for i in range(1, n+1):
    tmp=raw_input("")
    A, B = map(int, tmp.split(" "))
    result = solve(A, B)
    print "Case #%d: %d" % (i, result)


