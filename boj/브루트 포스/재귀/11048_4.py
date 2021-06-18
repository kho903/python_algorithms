import sys

sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
a = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
d = [[-1] * (m + 1) for _ in range(n + 1)]


def solve(i, j):
    if i > n or j > m:
        return 0
    if d[i][j] >= 0:
        return d[i][j]
    d[i][j] = max(solve(i + 1, j), solve(i, j + 1)) + a[i][j]
    return d[i][j]


print(solve(1, 1))
