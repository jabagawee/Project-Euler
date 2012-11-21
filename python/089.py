f = open("roman.txt").read().split()

# stolen from tim valenta on code.activestate.com
numeral_map = zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
)

def r2n(roman):
    i, result = 0, 0
    for integer, numeral in numeral_map:
        while roman[i:i+len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result


def n2r(num):
    result = []
    for integer, numeral in numeral_map:
        count = int(num/integer)
        result.append(numeral*count)
        num -= integer*count
    return ''.join(result)

print sum([len(x) - len(n2r(r2n(x))) for x in f])
