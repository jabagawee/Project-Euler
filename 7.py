#! /usr/bin/env python

from util import prime_generator

if __name__ == "__main__":
    counter = 0
    gen = prime_generator()
    while True:
        prime = gen.next()
        counter += 1
        if counter == 10001:
            print prime
            break
