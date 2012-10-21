# Check http://stackoverflow.com/questions/10232306/using-floyd-warshall-algorithm-to-count-number-of-paths-between-2-vertices
# Ineffective for large inputs (Contet analysis says this should suffice though)

T = int(raw_input(""))

for t in range(1, T+1):
    N = int(raw_input(""))
    route = [[0] * N for i in range(N)]

    for n in range(0, N):
        Ms = map(int, raw_input("").split(" "))
        for m in range(1, Ms[0]+1):
            route[n][Ms[m]-1] = 1

    flag = False
    for k in range(0, N):
        for i in range(0, N):
            for j in range(0, N):
                route[i][j] = route[i][j] + route[i][k] * route[k][j]

    for i in range(0, N):
        for j in range(0, N):
            if route[i][j] > 1:
                flag = True
    if flag:
        print "Case #%d: Yes" % t
    else:
        print "Case #%d: No" % t

    

