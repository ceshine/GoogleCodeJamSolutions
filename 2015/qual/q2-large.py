import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        N = int(f.readline())
        for i in xrange(1, N+1):
            D = int(f.readline())
            pis = map(int, f.readline().split(" "))
            ans = 1001
            for target in xrange(1, 1001):
                count = 0
                for p in pis:
                    count += p/target -1
                    if p%target > 0:
                        count += 1
                ans = min(count+target, ans)
            print "Case #{}: {}".format(i, ans) 
