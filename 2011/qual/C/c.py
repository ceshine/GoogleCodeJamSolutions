import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
	N = int(sys.stdin.readline())
	nums = map(int, sys.stdin.readline().split(" "))
	xorsum = 0
	for n in range(0,N):
            xorsum ^= nums[n]
        if xorsum != 0:
            print "Case #%d: NO" % (t)
        else:
            sums = sum(nums)
            nums.sort()
            print "Case #%d: %d" % (t, sums-nums[0])


if __name__ == "__main__":
    main()
