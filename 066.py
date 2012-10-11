def find_minimal_x(D):
    x = 2
    while True:
        for y in xrange(1, x):
            if x**2 - D * y**2 == 1:
                return x
        x += 1

best_D = 0
best_x = 0

for D in xrange(1,1000+1):
    tmp = find_minimal_x(D)
    if tmp > best_x:
        best_x = tmp
        best_D = D

print best_D
