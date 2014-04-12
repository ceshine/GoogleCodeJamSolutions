def simulate(C, F, X, builds):
    rate = 2
    time = 0
    while builds:
        time += C / rate
        rate += F
        builds -= 1
    return time + X / rate


if __name__ == "__main__":
    T = int(raw_input(""))
    for t in xrange(1, T+1):
        C, F, X = map(float, raw_input("").split(" "))
        best_time = X / 2
        builds = 1
        while True:
            time = simulate(C, F, X, builds)
            if time > best_time:
                builds = builds / 2 + 1
                break
            builds *= 2
            best_time = time
        while True:
            time = simulate(C, F, X, builds)
            if time > best_time:
                break            
            builds += 1
            best_time = time        
        print "Case #%d: %.7f" % (t, best_time)

        
