from fractions import Fraction

ans = 1

for num in xrange(10, 99+1):
    for den in xrange(num+1, 99+1):
        n, d = [num/10, num%10], [den/10, den%10]
        common = set(n).intersection(set(d))
        if common:
            common = common.pop()
            if common != 0:
                n.remove(common)
                d.remove(common)
                if d[0] != 0 and Fraction(num, den) == Fraction(n[0], d[0]):
                    ans *= Fraction(num, den)

print ans
