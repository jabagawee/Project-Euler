def is_incr(n):
    n = str(n)
    if len(n) == 1:
        return True
    return n[1] >= n[0] and is_incr(n[1:])

def is_decr(n):
    n = str(n)
    if len(n) == 1:
        return True
    return n[1] <= n[0] and is_decr(n[1:])

def is_bouncy(n):
    return not is_incr(n) and not is_decr(n)

bouncy = 0
x = 1
done = False

while not done:
    bouncy += 1 if is_bouncy(x) else 0
    if float(bouncy) / (x) == 0.99:
        print x
        done = True
    x += 1
