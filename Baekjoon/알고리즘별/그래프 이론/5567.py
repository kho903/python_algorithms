from collections import deque

n = int(input())
m = int(input())
a = [[] * n for _ in range(n)]
for i in range(m):
    r, s = map(int, input().split())
    a[r - 1].append(s - 1)
    a[s - 1].append(r - 1)


def bfs(x):
    visited = [0] * n
    visited[x] = 1
    q.append(x)
    while q:
        x = q.popleft()
        for i in a[x]:
            if not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
    return visited


q = deque()
res = bfs(0)
cnt = 0
for z in res:
    if 1 < z <= 3:
        cnt += 1
print(cnt)
