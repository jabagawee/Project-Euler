#! /usr/bin/env python

if __name__ == "__main__":
    max_palindrome = 0

    for x in xrange(900, 999 + 1):
        for y in xrange(900, 999 + 1):
            xy = x * y
            if str(xy) == str(xy)[::-1] and xy > max_palindrome:
                max_palindrome = xy

    print max_palindrome
