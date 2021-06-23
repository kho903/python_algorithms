n, m = map(int, input().split())
d = [[0] * (m + 1) for _ in range(n + 1)]
d[1][1] = 1
mod = 1000000007
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if not (i == 1 and j == 1):
            d[i][j] = (d[i][j - 1] + d[i - 1][j] + d[i - 1][j - 1]) % mod

print(d[n][m])
