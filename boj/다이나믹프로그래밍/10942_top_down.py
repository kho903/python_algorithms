import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
d = [[-1] * n for _ in range(n)]


def solve(i, j):
    if i == j:
        return 1
    elif i + 1 == j:
        if a[i] == a[j]:
            return 1
        else:
            return 0
    if d[i][j] != -1:
        return d[i][j]
    if a[i] != a[j]:
        d[i][j] = 0
    else:
        d[i][j] = solve(i + 1, j - 1)
    return d[i][j]


m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(solve(s - 1, e - 1))
