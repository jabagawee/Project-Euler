def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def even(seq):
    for num in seq:
        if num % 2 == 0:
            yield num

def stop_at_n(seq, n):
    for num in seq:
        if num > n:
            break
        yield num

print sum(even(stop_at_n(fib(), 4000000)))
