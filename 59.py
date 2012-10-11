from itertools import izip

f = map(int, open("cipher1.txt").read().split(','))

def main():
    for a in xrange(ord('a'), ord('z') + 1):
        for b in xrange(ord('a'), ord('z') + 1):
            for c in xrange(ord('a'), ord('z') + 1):
                key = [a, b, c] 
                key *= len(f)/len(key) + 1
                plaintext = ''.join(map(chr,[x ^ y for x, y in izip(f, key)]))
                if ' the ' in plaintext:
                    print plaintext
                    print sum([ord(x) for x in plaintext])
                    return

if __name__ == "__main__":
    main()
