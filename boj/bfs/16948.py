from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]
dist = [[-1] * 200 for _ in range(200)]
q = deque()
q.append((r1, c1))
dist[r1][c1] = 0
while q:
    x, y = q.popleft()
    for k in range(6):
        nx, ny = x + dr[k], y + dc[k]
        if 0 <= nx < n and 0 <= ny < n:
            if dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
print(dist[r2][c2])
