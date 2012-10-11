from util import d

abundant_nums = [x for x in xrange(2, 20161+1) if d(x) > x]

ans = set(range(1, 20161+1))

for x in abundant_nums:
    for y in abundant_nums:
        if x + y > 20161:
            break
        ans.discard(x+y) 

print sum(ans)
