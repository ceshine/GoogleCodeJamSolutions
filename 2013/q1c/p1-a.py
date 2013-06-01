vowels = ['a', 'e', 'i', 'o', 'u']

def runCase():
    name, n = raw_input("").split()
    n = int(n)
    m = len(name)
    count = 0
    for i in range(0, m):
        for j in range(i+n,m+1):
            t_str = name[i:j]
            c_count = 0
            for ch in t_str:
                if ch in vowels:
                    c_count = 0
                else:
                    c_count += 1
                    if c_count == n:
                        count += 1
                        #print i, j, t_str
                        break
    

    return count
    
def main():
    n = int(raw_input(""))
    
    for i in range(1, n+1):
        result = runCase()
        print "Case #%d: %d" % (i, result)
            

main()