import sys

def cal_moves(seq):
    total = 0
    loc = {'O':1, 'B':1}
    step = {'O':0, 'B':0}
    for idx in range(0,len(seq)):
        robot = seq[idx][0]
        button = int(seq[idx][1])
	move = 0
        if step[robot] >= abs(button - loc[robot]):
            move = 1;
        else:
            move = abs(button - loc[robot]) - step[robot] + 1
	total += move
        step['O'] += move
        step['B'] += move
        step[robot] = 0
        loc[robot] = button
    return total

def main():
    N = int(sys.stdin.readline())
    for n in range(1,N+1):
        seq = []
        moves = sys.stdin.readline().split(" ")
        for i in range(1, len(moves), 2):
            seq.append((moves[i],moves[i+1]))
        result = cal_moves(seq)
        print "Case #%d: %d" % (n, result)
    
if __name__ == '__main__':
    main()
