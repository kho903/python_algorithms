import sys
sys.setrecursionlimit(100000)
n, m, k = map(int, input().split())
a = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[False] * (m + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    a[x][y] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    visited[x][y] = True
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 < nx <= n and 0 < ny <= m:
            if a[nx][ny] == 1 and visited[nx][ny] == False:
                dfs(nx, ny)


res = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j] == 1 and visited[i][j] == False:
            cnt = 0
            dfs(i, j)
            res = max(res, cnt)

print(res)
