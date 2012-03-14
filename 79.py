f = open('keylog.txt').read().strip().split('\n')

# topological sorting from wikipedia
L = []
V, E = set(), set()
for attempt in f:
    for k in attempt:
        V.add(k)
    E.add((attempt[0],attempt[1]))
    E.add((attempt[1],attempt[2]))


S = [y for y in V if y not in [x[0] for x in E]]

def visit(n):
    if n in V:
        V.remove(n)
        for m in [y for y in V if y in [x[0] for x in E if x[1] == n]]:
            visit(m)
        L.append(n)

for n in S:
    visit(n)

print L
