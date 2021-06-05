def f1(a):
    n = len(a)
    m = len(a[0])
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = a[n - i - 1][j]
    return arr


def f2(a):
    n = len(a)
    m = len(a[0])
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = a[i][m - j - 1]
    return arr


def f3(a):
    n = len(a)
    m = len(a[0])
    arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr[j][n - i - 1] = a[i][j]
    return arr


def f4(a):
    n = len(a)
    m = len(a[0])
    arr = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            arr[m - j - 1][i] = a[i][j]
    return arr


def f5(a):
    n = len(a)
    m = len(a[0])
    arr = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            arr[i][j + m // 2] = a[i][j]
            arr[i + n // 2][j + m // 2] = a[i][j + m // 2]
            arr[i + n // 2][j] = a[i + n // 2][j + m // 2]
            arr[i][j] = a[i + n // 2][j]
    return arr


def f6(a):
    n = len(a)
    m = len(a[0])
    arr = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            arr[i][j + m // 2] = a[i + n // 2][j + m // 2]
            arr[i + n // 2][j + m // 2] = a[i + n // 2][j]
            arr[i + n // 2][j] = a[i][j]
            arr[i][j] = a[i][j + m // 2]
    return arr


n, m, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
num = list(map(int, input().split()))

f = [f1, f2, f3, f4, f5, f6]
for i in num:
    a = f[i - 1](a)
for row in a:
    print(*row, sep=' ')
