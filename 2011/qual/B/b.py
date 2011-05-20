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
	elif i != len(origin)-1 and not comb.has_key(origin[i+1]+current) and oppose.has_key(current):
	    for j in range(0,len(result)):
		if oppose.get(result[j]) and current in oppose[result[j]]:
		    result= []
		    current = None
		    break
        if current != None:
    	    result.append(current)
    	print result, origin[i+1:]
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
	    if not oppose.has_key(tmp[0]):
                oppose[tmp[0]] = []
            oppose[tmp[0]].append(tmp[1])
	    if not oppose.has_key(tmp[1]):
                oppose[tmp[1]] = []
            oppose[tmp[1]].append(tmp[0])
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
