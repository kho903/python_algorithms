from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

t = int(input())
for _ in range(t):
    l = int(input())
    q = deque()
    dist = [[0] * l for _ in range(l)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            break
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < l and 0 <= ny < l:
                if dist[nx][ny] == 0:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
        if dist[ex][ey] > 0:
            break
    print(dist[ex][ey])
