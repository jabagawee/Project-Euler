def f(n):
    ans = n
    while not all([x in '012' for x in str(ans)]):
        ans += n
    return ans

print sum([f(n)/n for n in xrange(1, 10000+1)])
