mp = 0 # max palindrome

for x in xrange(900, 999+1):
    for y in xrange(900, 999+1):
        a = x * y
        if str(a) == str(a)[::-1] and a > mp:
            mp = a

print mp
