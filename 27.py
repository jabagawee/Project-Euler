from util import is_prime

def awesomeness(a, b):
    n = 0
    while is_prime(n**2 + a * n + b):
        n += 1
    return n

ma, ans = 0, 0 # max awesomeness, answer
for a in xrange(-999, 999+1):
    for b in xrange(-999, 999+1):
        ca = awesomeness(a, b) # current awesomeness
        if ca > ma:
            ma, ans = ca, a * b

print ans
