from math import log

f = [x.split(',') for x in open('base_exp.txt').read().split('\n')]

good_line, max_val = 0, 0
for line_num, pair in enumerate(f):
    val = int(pair[1]) * log(float(pair[0]))
    if val > max_val:
        good_line, max_val = line_num + 1, val

print good_line
