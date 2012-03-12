from util import prime_factorize

x = 2
while True:
    x1, x2, x3, x4 = x, x+1, x+2, x+3
    if map(len, map(prime_factorize, (x1, x2, x3, x4))) == [4, 4, 4, 4]:
        print x1
        break
    x += 1
