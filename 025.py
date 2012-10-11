from util import fib_gen

g, count = fib_gen(), 0
a = g.next()
while len(str(a)) < 1000:
    count += 1
    a = g.next()

print count
