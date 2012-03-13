target = 100
fillers = xrange(1,99+1)
ways = [0] * (target + 1)
ways[0] = 1

for filler in fillers:
    for x in xrange(filler, target + 1):
        ways[x] += ways[x - filler]

print ways[target]
