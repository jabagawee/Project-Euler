target = 200
coin_denoms = (1, 2, 5, 10, 20, 50, 100, 200)
ways = [0] * (target + 1)
ways[0] = 1

for coin in coin_denoms:
    for x in xrange(coin, target + 1):
        ways[x] += ways[x - coin]

print ways[target]
