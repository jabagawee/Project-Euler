def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def even(seq):
    for n in seq:
        if n % 2 == 0:
            yield n

def stop_at_n(seq, limit):
    for n in seq:
        if n > limit:
            break
        yield n

print sum(even(stop_at_n(fib(), 4000000)))
