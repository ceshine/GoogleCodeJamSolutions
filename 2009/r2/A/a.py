#!/usr/bin/python
from sys import stdin

def main():
    T = int(stdin.readline())
    for t in range(1, T+1):
	N = int(stdin.readline())
	matrix = [ 0 for i in range(0, N)]
        for n in range(0, N):
	    tmp = stdin.readline()
	    cnt = 0
	    for c in tmp:
		if c =='1':
		    matrix[n] = cnt
		cnt += 1
	allocate = [ -1 for i in range(0, N)]
	for i in range(0, N):
	    for j in range(0, N):
		if allocate[j] == -1 and matrix[j] <= i:
		    allocate[j] = i
		    break
	
	min_swap = 0
	for i in range(0 ,N):
	    for j in range(i+1, N):
		if allocate[i] > allocate[j]:
		    min_swap += 1

	print "Case #%d: %d" % (t, min_swap)

if __name__=="__main__":
    main()
