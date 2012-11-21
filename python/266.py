from math import sqrt
from util import primesfrom2to, product, proper_divisors

p = product([int(x) for x in list(primesfrom2to(190))])
print max(filter(lambda x: x < sqrt(p), proper_divisors(p)))
