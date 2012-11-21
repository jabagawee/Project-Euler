def is_reversible(n):
    if n % 10 == 0:
        return False
    n += int(str(n)[::-1])
    for even in '24680':
        if even in str(n):
            return False
    return True

ans = 0

for x in xrange(1000000000):
    if x % 100000 == 0:
        print x
    ans += 1 if is_reversible(x) else 0

print ans
