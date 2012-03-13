from itertools import permutations

p = permutations('1234567890')
ans = 0

for d in p:
    d = ''.join(d)
    if int(d[3]) % 2 == 0 and \
       int(d[2:5]) % 3 == 0 and \
       int(d[5]) % 5 == 0 and \
       int(d[4:7]) % 7 == 0 and \
       int(d[5:8]) % 11 == 0 and \
       int(d[6:9]) % 13 == 0 and \
       int(d[7:10]) % 17 == 0:
        ans += int(d)

print ans
