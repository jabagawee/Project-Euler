def is_lychrel(n):
    for x in xrange(50-1):
        n += int(str(n)[::-1])
        if str(n) == str(n)[::-1]:
            return False
    return True

print len([x for x in xrange(1, 10000) if is_lychrel(x)])
