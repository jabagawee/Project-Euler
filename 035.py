from util import is_prime

def circular(n):
    for x in xrange(len(str(n))):
        num = int(str(n)[x:] + str(n)[:x])
        if not is_prime(num):
            return False
    return True

print len([x for x in xrange(1000000) if circular(x)])
