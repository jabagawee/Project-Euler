from util import is_prime

counter, n = 0, 0

while True:
    n += 1
    if is_prime(n):
        counter += 1
        if counter == 10001:
            break

print n
