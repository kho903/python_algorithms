n = int(input())
res = []
for _ in range(n):
    res.append(list(map(int, input().split())))

res.sort(key=lambda x: (x[1], x[0]))
for r in res:
    print(r[0], r[1])
