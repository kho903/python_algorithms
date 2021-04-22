n = int(input()) + 1
t = int(input())
com = [[0] * n for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(t):
    a, b = map(int, input().split())
    com[a][b] = 1
    com[b][a] = 1


def dfs(v):
    visited[v] = 1
    for i in range(n):
        if com[v][i] == 1 and visited[i] == 0:
            dfs(i)


dfs(1)
count = 0
for v in visited:
    if v == 1:
        count += 1
print(count - 1)
