n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

d = [0] * m
check = [False] * n


def solve(selected, n, m):
    if selected == m:
        print(' '.join(map(str, d)))
        return
    for i in range(n):
        if not check[i]:
            d[selected] = a[i]
            check[i] = True
            solve(selected + 1, n, m)
            check[i] = False


solve(0, n, m)
