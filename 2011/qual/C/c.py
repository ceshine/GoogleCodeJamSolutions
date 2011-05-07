import sys

def find_overlap(nums):
    table = [{0:''}]
    for i in range(1,len(nums)+1):
        newentry = {}
        for key in table[i-1].keys():
            newentry[nums[i-1]^key] = ''
    results = []
    for a in range(1, len(nums)/2+1):
        b = len(nums)-a
        for key in table[a].keys():
            if table[b].has_key(key):
                
def construct_table(nums):
    table = {0:{0:''}}
    for i in range(0,len(nums)):
        for item in table.keys():
            newnum = item^nums[i]
            if not table.has_key(newnum):
                table[newnum] = {}
            for totals in table[item].keys():
                table[newnum][totals+nums[i]] = ''                
    return table

def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
	N = int(sys.stdin.readline())
	nums = map(int, sys.stdin.readline().split(" "))
	sums = sum(nums)
	table = construct_table(nums)
        #print table, sums
        result = -1
        for xorvalue in table.keys():
            for total in table[xorvalue].keys():
                if total != sums and total != 0 and table[xorvalue].has_key(sums-total):
                    result = max([result,max([total,sums-total])])
        if result == -1:
	    print "Case #%d: NO" % (t)
	else:
	    print "Case #%d: %d" % (t, result)

if __name__ == "__main__":
    main()
