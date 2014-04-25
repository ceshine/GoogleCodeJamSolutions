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
        builds = 0
        while True:
            step = 1
            while True:
                builds += step
                time = simulate(C, F, X, builds)
                previous = simulate(C, F, X, builds-1)
                if time > best_time or time > previous:
                    builds = builds - step
                    break
                step *= 2
                best_time = time
            if step == 1:
                break
                
        print "Case #%d: %.7f" % (t, best_time)

        
