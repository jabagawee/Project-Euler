#! /usr/bin/env python

from util import fib_gen


def even(seq):
    for n in seq:
        if n % 2 == 0:
            yield n


def stop_at_n(seq, limit):
    for n in seq:
        if n > limit:
            break
        yield n

if __name__ == "__main__":
    print sum(even(stop_at_n(fib_gen(), 4000000)))
