def validCanvas(canvas, n, m):
    #check horizontal
    for i in range(0, n):
        flag = True
        for j in range(0, m):
            if canvas[i][j] == 0:
                flag = False
                break
        if flag:
            for j in range(0, m):
                canvas[i][j] = 2

    #check vertical
    for i in range(0, m):
        flag = True
        for j in range(0, n):
            if canvas[j][i] == 0:
                flag = False
                break
        if flag:
            for j in range(0, n):
                canvas[j][i] = 2

    #check validity
    for i in range(0, n):
        for j in range(0, m):
            if canvas[i][j] == 1:
                return False
    return True

def runCase():
    n, m = map(int, raw_input("").split())
    lawn = []
    for i in range(0, n):
        lawn.append(map(int, raw_input("").split()))
    
    dset = set([])
    for i in range(0, n):
        for j in range(0, m):
            dset.add(lawn[i][j])
    
    for i in sorted(dset, reverse = True):
        canvas = [[0 for k in range(0, m)] for j in range(0, n)]
        for j in range(0, n):
            for k in range(0, m):
                if lawn[j][k] <= i:
                    canvas[j][k] = 1
#        print canvas
        if not validCanvas(canvas, n, m):
            return False

    return True




n = int(raw_input(""))
for i in range(1, n+1):
    possible = runCase()
    if possible:
        txt = "YES"
    else:
        txt = "NO"
    print "Case #%d: %s" % (i, txt)
