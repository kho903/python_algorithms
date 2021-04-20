inp = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]
res = 0
for coin in coins:
    if coin <= inp:
        res += inp // coin
        inp %= coin

print(res)