def jump(current, x, y, cx, cy, str, max_move):
    if current == max_move:
        if x == cx and y == cy:
            return str
        else:
            return None
    
    if x != cx:
        n_str = jump(current+1, x+current+1, y, cx, cy, str+"E", max_move)
        if n_str:
            return n_str
        n_str = jump(current+1, x-current-1, y, cx, cy, str+"W", max_move)
        if n_str:
            return n_str
    
    if y != cy:
        n_str = jump(current+1, x, y+current+1, cx, cy, str+"N", max_move)
        if n_str:
            return n_str
        n_str = jump(current+1, x, y-current-1, cx, cy, str+"S", max_move)
        if n_str:
            return n_str
    return None
    
def runCase():
    x, y = map(int, raw_input("").split())
    for i in range(1, 100):
        print i
        str = jump(0, 0, 0, x, y, "", i)
        if str:
            return str
    return "None Found"
    


def main():
    n = int(raw_input(""))
    
    for i in range(1, n+1):
        result = runCase()
        print "Case #%d: %s" % (i, result)
            

main()