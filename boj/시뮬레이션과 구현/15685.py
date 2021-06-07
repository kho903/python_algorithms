c = [[False] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def curve(x, y, d, gen):
    ans = [d]
    for g in range(1, gen + 1):
        temp = ans[::-1]
        for i in range(len(temp)):
            temp[i] = (temp[i] + 1) % 4
        ans += temp
    return ans


n = int(input())
for _ in range(n):
    y, x, d, gen = map(int, input().split())
    dirs = curve(x, y, d, gen)
    c[x][y] = True
    for dr in dirs:
        x += dx[dr]
        y += dy[dr]
        c[x][y] = True

ans = 0
for i in range(100):
    for j in range(100):
        if c[i][j] and c[i][j + 1] and c[i + 1][j] and c[i + 1][j + 1]:
            ans += 1
print(ans)
