from math import log10

def num_digits(n):
    return int(log10(n)) + 1

ans = 0

for base in xrange(1, 10):
    for power in xrange(1, 21+1): # magicks
        if num_digits(base**power) == power:
            ans += 1

print ans
