LIMIT = 50
NORAD, RAD = 0, 1

p0 = (0, 0)

one = [(x,y) for x in xrange(LIMIT+1) for y in xrange(LIMIT+1)]
two = [(x,y) for x in xrange(LIMIT+1) for y in xrange(LIMIT+1)]

def dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2, RAD

def is_right_triangle(d1, d2, d3):
    return d1[0] + d2[0] == d3[0] or d2[0] + d3[0] == d1[0] or d1[0] + d3[0] == d2[0]

ans = 0

for p1 in one:
    if p1 != p0:
        for p2 in two:
            if p2 != p1 and p2 != p0:
                d1, d2, d3 = dist(p1, p2), dist(p1, p0), dist(p2, p0)
                if is_right_triangle(d1, d2, d3):
                    ans += 1

print ans/2
