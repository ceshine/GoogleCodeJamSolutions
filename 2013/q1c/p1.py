vowels = ['a', 'e', 'i', 'o', 'u']

def runCase():
    name, n = raw_input("").split()
    n = int(n)
    count = 0
    v_len = 0
    c_len = 0
    for i in range(0, len(name)):
        if name[i] in vowels:
            if c_len > 0:
                if c_len >= n:
                    count += (len(name) - i + 1) * (v_len + 1) - 1  + (len(name) - i )  * (c_len - n) + v_len * (c_len - n) + (c_len - n + 1) * (c_len - n + 2) / 2
                    v_len = n - 1
                    #print count, (len(name) - i + 1) * (v_len + 1), (len(name) - i )  * (c_len - n), v_len * (c_len - n) , (c_len - n + 1) * (c_len - n + 2) / 2
                    #print count
                else:
                    v_len += c_len
                c_len = 0
            v_len += 1
        else:
            c_len += 1
    if c_len >= n:
        count += v_len  + v_len * (c_len - n) + (c_len - n + 1) * (c_len - n + 2) / 2
    return count


def main():
    n = int(raw_input(""))
    
    for i in range(1, n+1):
        result = runCase()
        print "Case #%d: %d" % (i, result)
            

main()