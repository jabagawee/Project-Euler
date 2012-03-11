from util import is_prime

num = 600851475143
while not is_prime(num):
    for x in xrange(2, num):
        if num % x == 0:
            num /= x
            break

print num
