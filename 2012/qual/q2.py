from math import log

n = int(raw_input(""))

for nn in range(1,n+1):
    tmp=raw_input("")
    a, b = map(int, tmp.split(" "))

    digit = int(log(a)/log(10))

    total = 0

    for i in range(a, b+1):
        d = {}
        for j in range(1,digit+1):
            trans = i / (10**j) + (i % (10**j) * (10**(digit-j+1)))
            if trans <= b and trans >= a and trans != i:
                if not d.has_key(trans):
                    d[trans] = 1
                    total += 1
                   # print i, trans

    print "Case #%d: %d" % (nn,total/2)
