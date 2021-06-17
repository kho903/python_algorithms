n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
d = []
check = []
visited = [False] * n


def solve(num):
    if num == m:
        temp = ' '.join(map(str, d))
        if temp not in check:
            check.append(temp)
        return
    for i in range(n):
        if num == 0 or not visited[i]:
            d.append(a[i])
            visited[i] = True
            solve(num + 1)
            visited[i] = False
            d.pop()


solve(0)

for i in check:
    print(i)
