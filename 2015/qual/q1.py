import sys

if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        N = int(f.readline())
        for i in xrange(1, N+1):
            SMAX, S_LIST = f.readline().split()
            standing = int(S_LIST[0])
            needed = 0
            for s, count in enumerate(S_LIST[1:]):
                count = int(count)
                if standing < s + 1:
                    needed += s + 1 - standing
                    standing += s + 1 - standing
                standing += count
            print "Case #{}: {}".format(i, needed)
