def get_arrangement():
    result = []
    for i in range(4):
        result.append(map(int, raw_input("").split(" ")))
    return result

if __name__ == "__main__":
    T = int(raw_input(""))
    for t in xrange(1, T+1):
        ans1 = int(raw_input(""))
        arrange1 = get_arrangement()
        ans2 = int(raw_input(""))
        arrange2 =get_arrangement()
        set1 = set(arrange1[ans1-1])
        set2 = set(arrange2[ans2-1])
        magic = set1 & set2
        if len(magic) == 0:
            result = "Volunteer cheated!"
        elif len(magic) > 1:
            result = "Bad magician!"
        else:
            result = str(list(magic)[0])
        print "Case #%d: %s" % (t, result)
