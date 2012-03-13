from math import sqrt

def is_pentagonal(n):
    t = (sqrt(1 + 24 * n) + 1) / 6
    return int(t) == t

j = 1
done = False
while not done:
    j += 1
    P_j = j * (3 * j - 1) / 2

    for k in xrange(j - 1, 1 - 1, -1):
        P_k = k * (3 * k - 1) / 2
        if is_pentagonal(P_j - P_k) and is_pentagonal(P_j + P_k):
            print P_j - P_k
            done = True
            break
