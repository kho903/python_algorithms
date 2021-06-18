n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * m for _ in range(n)]
d[0][0] = a[0][0]
for i in range(n):
    for j in range(m):
        if j + 1 < m and d[i][j + 1] < d[i][j] + a[i][j + 1]:
            d[i][j + 1] = d[i][j] + a[i][j + 1]
        if i + 1 < n and d[i + 1][j] < d[i][j] + a[i + 1][j]:
            d[i + 1][j] = d[i][j] + a[i + 1][j]
print(d[n - 1][m - 1])
