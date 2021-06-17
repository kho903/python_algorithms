n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
d = []


def solve(num):
    if num == m:
        print(' '.join(map(str, d)))
        return
    for i in range(n):
        if num == 0 or d[num - 1] <= a[i]:
            d.append(a[i])
            solve(num + 1)
            d.pop()


solve(0)
