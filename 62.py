def is_cube(n):
    return abs(n**(1./3) - int(n**(1./3)))

print is_cube(1)
print is_cube(41063625)
print is_cube(56623104)
print is_cube(66430125)
