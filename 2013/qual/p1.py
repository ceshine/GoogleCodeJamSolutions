def isFull(board):
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == '.':
                return False
    return True

def winner(comp):
    count = [0,0,0] # O X T
    for i in range(0, 4):
        if comp[i] == 'T':
            count[2] = 1
        elif comp[i] == 'O':
            count[0] = count[0] + 1
        elif comp[i] == 'X':
            count[1] = count[1] + 1
    
    if count[0] + count[2] == 4: # O won
        return 'O'
    elif count[1] + count[2] == 4: # X won
        return 'X'
    return None

def runCase():
    board = []
    for i in range(0,4):
        row = raw_input("")
        board.append(row)

    #check horizontal
    for i in range(0,4):
        w = winner(board[i])
        if w:
            return w

    #check vertical
    for i in range(0,4):
        w = winner([board[0][i], board[1][i], board[2][i], board[3][i]])
        if w:
            return w

    #check diagonal
    w = winner([board[0][0], board[1][1], board[2][2], board[3][3]])
    if w:
        return w
    w = winner([board[3][0], board[2][1], board[1][2], board[0][3]])
    if w:
        return w

    if isFull(board):
        return "TIE"
    else:
        return "NOT FINISHED"

n = int(raw_input(""))
for i in range(1, n+1):
    result = runCase()
    if result == "O" or result == 'X':
        print "Case #%d: %s won" % (i, result)
    elif result == "TIE":
        print "Case #%d: Draw" % i
    elif result == "NOT FINISHED":
        print "Case #%d: Game has not completed" % i
    if i != n:
        empty_line = raw_input("")

