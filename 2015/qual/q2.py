import sys
import math
from collections import defaultdict

cache = {}
def serialize_pancakes(pancakes, n):
    return " ".join(map(str, pancakes[:n+1]))

def search(pancakes, n, specials):
    if n <= 3:
        return specials + n
    best, best_divisor = n + specials, 1
    for divisor in range(2, n-1):
        k = max((j if pancakes[j] else 0 for j in xrange(n)))
        max_product = n / divisor
        if n % divisor > 0:
            max_product += 1
        local_specials = (divisor - 1) * pancakes[n]
#        print n, k, best, max_product, local_specials
        new_pancakes = pancakes[:]
        new_pancakes[n/divisor] += pancakes[n] * (divisor-n%divisor)
        new_pancakes[n/divisor+1] += pancakes[n] * (n%divisor) 
        new_pancakes[n] = 0
        identifier = serialize_pancakes(new_pancakes, max(k, max_product))
        if identifier in cache:
            local_result = cache[identifier] + local_specials + specials
        else:
            local_result = search(new_pancakes, max(k, max_product), local_specials + specials)
            cache[identifier] = local_result - local_specials - specials
        if local_result < best:
#            print k, divisor
            best = local_result
    return best


if __name__ == '__main__':
    filename = sys.argv[1]
    with open(filename) as f:
        N = int(f.readline())
        for i in xrange(1, N+1):
            D = int(f.readline())
            pis = map(int, f.readline().split(" "))
            pancakes = [0] * (max(pis) + 1)
            for pi in pis:
                pancakes[pi] += 1
            print "Case #{}: {}".format(i, search(pancakes, len(pancakes)-1, 0))
#             specials = 0
#             best = len(pancakes) - 1 
#             for j in xrange(len(pancakes)-1, 3, -1):
#                 if pancakes[j] == 0:
#                     continue
#                 for k in xrange(j-1, 0, -1):
#                     if pancakes[k] > 0:
#                         break
#                 local_best, local_best_divisor = -1, -1
#                 for divisor in range(2, j-1):
#                     max_product = j/divisor
#                     if j % divisor > 0:
#                         max_product += 1
#                     local_specials = (divisor - 1) * pancakes[j] + specials
#                     if local_best == -1 or max(max_product, k) + local_specials  < local_best:
#                         local_best = max(max_product, k) + local_specials
#                         local_best_divisor = divisor
# #                if local_best == -1 or local_best > best:
# #                    print local_best, j
#                     #break
#                 specials += (local_best_divisor-1) * pancakes[j]
#                 pancakes[j/local_best_divisor] += pancakes[j] * (local_best_divisor-j%local_best_divisor)
#                 pancakes[j/local_best_divisor+1] += pancakes[j] * (j%local_best_divisor)
#                 pancakes[j] = 0
#                 if best > local_best:
#                     best = local_best
#             #print "Case #", i, pis, best

