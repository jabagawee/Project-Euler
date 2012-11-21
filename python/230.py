from functools import partial
from itertools import count

class MemoizedGenerator(object):
    def __init__(self, gen):
        self.__gen = gen
        self.__cache = []
        self.__iter = None
        self.__empty = False

    def __call__(self, *args, **kwargs):
        if not (self.__empty or self.__iter):
            self.__iter = self.__gen(*args, **kwargs)
        for n in count():
            if n < len(self.__cache):
                yield self.__cache[n]
            elif self.__empty:
                break
            else:
                try:
                    term = next(self.__iter)
                except StopIteration:
                    self.__empty = True
                    break
                else:
                    self.__cache.append(term)
                    yield term

@MemoizedGenerator
def F(A, B):
    while True:
        yield A
        B, A = A, int(''.join([str(A), str(B)]))

def D(A, B, n):
    f = F(A, B)
    term = f.next()
    while len(str(term)) < n:
        term = f.next()
    return int(str(term)[n-1])

DEBUG = False

if DEBUG:
    print D(1415926535, 8979323846, 35)
else:
    A = 1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    B = 8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196
    
    print sum([10**x * D(A, B, 7**x * (127 + 19 * x)) for x in xrange(17+1)])
