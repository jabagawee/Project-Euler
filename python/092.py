def sum_square_digits(num):
    ret = 0
    while num > 0:
        ret += (num % 10) ** 2
        num /= 10
    return ret

ans = 0
cache = [0] * 10000003
cache[1] = 1
cache[89] = 89

for i in xrange(2, 10000000+1):
    temp = i
    while cache[temp] == 0:
        temp = sum_square_digits(temp)
    cache[i] = cache[temp]
    if cache[i] == 89:
        ans += 1

print ans
