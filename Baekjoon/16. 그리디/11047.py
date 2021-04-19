n, m = map(int, input().split())
coins = []
res = [0] * n
for _ in range(n):
    coins.append(int(input()))

coins.reverse()
i = 0
for coin in coins:
    res[i] = m // coin
    i += 1
    m %= coin

print(sum(res))
