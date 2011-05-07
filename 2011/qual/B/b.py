import sys

def trans(comb, oppose, origin):
    result = []
    for i in range(0, len(origin)):
	current = origin[i]
        if len(result) > 0 and comb.has_key(result[-1]+current):
	    newc = comb[result[-1]+current]
	    result = result[:-1]
	    result.append(newc)
	    current = None
	elif oppose.has_key(current):
	    for j in range(0,len(result)):
		if oppose.get(result[j])==current:
		    result= []
		    current = None
		    break
        if current != None:
    	    result.append(current)
    return result

def main():
    N = int(sys.stdin.readline())
    for n in range(1,N+1):
        comb = {}
	oppose = {}
        inputs = sys.stdin.readline().split(" ")
	C = int(inputs[0])
	for i in range(1,C+1):
	    tmp = inputs[i]
	    comb[tmp[0]+tmp[1]] = tmp[2]
	    comb[tmp[1]+tmp[0]] = tmp[2]
	D = int(inputs[C+1]) + C + 2
	for i in range(C+2, D):
	    tmp = inputs[i]
	    oppose[tmp[0]] = tmp[1]
	    oppose[tmp[1]] = tmp[0]
#	N = inputs[D]
	origin = inputs[D+1].strip()
	result = trans(comb, oppose, origin)
	
        text = "Case #%d: [" % n
	for item in result:
	    text += item + ", "
	if len(result) > 0:
	    text = text[:-2] + "]"
	else:
	    text += "]"
    	print text

if __name__ == '__main__':
    main()
