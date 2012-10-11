x = 1

while True:
    x2, x3, x4, x5, x6 = 2*x, 3*x, 4*x, 5*x, 6*x
    digits = map(tuple, map(sorted, map(str, (x, x2, x3, x4, x5, x6))))
    if len(set(digits)) == 1:
        print x
        break
    x += 1
