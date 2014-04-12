import copy

def war_optimal(naomi, ken):
    naomi = copy.copy(naomi)
    ken = copy.copy(ken)
    point = 0
    while len(naomi) and len(ken):
        if naomi[0] > ken[0]:
            point += 1
            naomi.pop(0)
            ken.pop(len(ken)-1)
        else:
            naomi.pop(0)
            ken.pop(0)
    return point
    
def deceitful_optimal(naomi, ken):
    naomi = copy.copy(naomi)
    ken = copy.copy(ken)
    point = 0
    while len(naomi) and len(ken):
        if naomi[len(naomi)-1] < ken[len(ken)-1]:
            naomi.pop(len(naomi)-1)
            ken.pop(0)
        else:
            naomi.pop(len(naomi)-1)
            ken.pop(len(ken)-1)
            point += 1
    return point

if __name__ == "__main__":
    T = int(raw_input(""))
    for t in xrange(1, T+1):
        N = int(raw_input(""))
        naomi = sorted(map(float, raw_input("").split(" ")), reverse=True)
        ken   = sorted(map(float, raw_input("").split(" ")), reverse=True)
        war_point = war_optimal(naomi, ken)
        deceitful_point = deceitful_optimal(naomi, ken)        
        print "Case #%d: %d %d" % (t, deceitful_point, war_point)


