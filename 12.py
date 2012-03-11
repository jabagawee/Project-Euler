from util import prime_factorize

def num_factors(n):
    factors = prime_factorize(n)
    if n == 1:
        return 1
    return reduce(lambda a, b: a * b, [x+1 for x in factors.values()])

triangle, adder = 0, 1
while True:
    triangle += adder
    adder += 1
    if num_factors(triangle) > 500:
        print triangle
        break
