from util import is_prime

for x in xrange(1000, 9999+1):
    if is_prime(x):
        perms = x, int(str(x)[1:]+str(x)[:1]), int(str(x)[2:]+str(x)[:2])
        if x == 1487:
            print perms[2]-perms[1] == perms[1]-perms[0]
        raw_input()
        if perms[2]-perms[1] == perms[1]-perms[0]:
            print 'found it'
