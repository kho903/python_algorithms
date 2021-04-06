n = int(input())
res = []
for _ in range(n):
    a, b = map(str, input().split())
    a = int(a)
    res.append([a, b])
res.sort(key=lambda x: (x[0]))
for r in res:
    print(r[0], r[1])
