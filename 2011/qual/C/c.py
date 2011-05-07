import sys

def construct_table(nums):
    table = []
    lib = {"".join(['0' for i in range(0,len(nums))]):(0,0)}
    table.append(lib)
    for i in range(1,len(nums)+1):
	lib = table[i-1]
        newlib = {}
	for j in range(0, len(nums)):
	    for key in lib.keys():
	        if key[j] == '0':
		    newkey =  key[:j] + '1' + key[j+1:]
		    if not newlib.has_key(newkey):
   		        newlib[newkey] = (lib[key][0]^nums[j],lib[key][1]+nums[j])
	table.append(newlib)
    return table

def invert_key(key):
    newkey = []
    for i in range(0,len(key)):
	if key[i] == '1':
	    newkey.append('0')
	else:
	    newkey.append('1')
    return "".join(newkey)

def find_max(table):
    levels = len(table)-1
    max_total = -1
    for a in range(1,levels/2+1):
	b = levels - a
        for key in table[a].keys():
	    invert = invert_key(key)
	    if table[b][invert][0] == table[a][key][0]:
		sean = max([table[b][invert][1],table[a][key][1]])
		if max_total < sean:
		    max_total = sean
    return max_total

def main():
    T = int(sys.stdin.readline())
    for t in range(1, T+1):
	N = int(sys.stdin.readline())
	nums = map(int, sys.stdin.readline().split(" "))
	table = construct_table(nums)
	result = find_max(table)
        
        if result == -1:
	    print "Case #%d: NO" % (t)
	else:
	    print "Case #%d: %d" % (t, result)

if __name__ == "__main__":
    main()
