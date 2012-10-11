ans, curr = 1, 1
SIZE = 1001

for x in xrange(1, (SIZE - 1) / 2 + 1):
    for y in xrange(4):
        curr += 2*x
        ans += curr

print ans
