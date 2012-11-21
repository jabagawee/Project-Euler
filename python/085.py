from util import combination

def rectangles(a, b):
    return combination(a + 1, 2) * combination(b + 1, 2)

best_xy, best_rects = 0, 0
for x in xrange(1, 2000):
    for y in xrange(1, 2000):
        rects = combination(x + 1, 2) * combination(y + 1, 2)
        if abs(rects - 2000000) < abs(best_rects - 2000000):
            best_rects = rects
            best_xy = x*y
        if rects > 2000000:
            break

print best_xy
