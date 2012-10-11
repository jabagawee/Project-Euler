f = sorted([name[1:-1] for name in open('names.txt').read().split(',')])

def score(word):
    return sum([ord(letter) - ord('A') + 1 for letter in word])

total = 0
for pos, name in enumerate(f):
    total += (pos + 1) * score(name)

print total
