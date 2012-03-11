from math import sqrt

def is_prime(n):
    if n % 2 == 0:
        return False
    for x in xrange(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True

num = 600851475143
while not is_prime(num):
    for x in xrange(2, num):
        if num % x == 0:
            num /= x
            break

print num
