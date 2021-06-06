dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
while True:
    if a[x][y] == 0:
        a[x][y] = 2
        cnt += 1
    if a[x + 1][y] != 0 and a[x - 1][y] != 0 and a[x][y - 1] != 0 and a[x][y + 1] != 0:
        if a[x - dx[d]][y - dy[d]] == 1:
            break
        else:
            x -= dx[d]
            y -= dy[d]
    else:
        d = (d + 3) % 4
        if a[x + dx[d]][y + dy[d]] == 0:
            x += dx[d]
            y += dy[d]

print(cnt)
