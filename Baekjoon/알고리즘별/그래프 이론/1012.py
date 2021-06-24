import sys

sys.setrecursionlimit(100000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == 1:
                a[nx][ny] = -1
                dfs(nx, ny)


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    a = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        y, x = map(int, input().split())
        a[x][y] = 1
    for i in range(n):
        for j in range(m):
            if a[i][j] > 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
