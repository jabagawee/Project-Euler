max_p, max_count = 120, 6

for p in xrange(121, 1000+1):
    curr_count = 0
    for a in xrange(1, p):
        for b in xrange(1, p-a):
            if a**2 + b**2 == (p-a-b)**2:
                curr_count += 1
    if curr_count > max_count:
        max_count, max_p = curr_count, p

print max_p
