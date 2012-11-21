f = filter(None, [''.join(x[4:].split('\n')) for x in open('sudoku.txt').read().strip().split('Grid')])

row = lambda index: index / 9
col = lambda index: index % 9
block = lambda index: (index / 27, index % 9 / 3)

shared = lambda a, b: row(a) == row(b) or col(a) == col(b) or block(a) == block(b)

def solve(puzzle):
    allowed = [set(xrange(1,9+1)) for x in xrange(81)]
    for i in xrange(81):
        if puzzle[i] != '0':
            allowed[i] = set()
            continue
        for j in xrange(81):
            if puzzle[j] != '0' and shared(i, j):
                allowed[i].discard(puzzle[j])
        if len(allowed[i]) == 1:
            puzzle[i] = allowed[i].pop()
    return puzzle

print f[0]
f[0] = solve(f[0])
print f[0]
