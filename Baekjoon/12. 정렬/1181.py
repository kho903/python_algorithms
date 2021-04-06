n = int(input())
res = []
for _ in range(n):
    res.append(input())
res = list(set(res))
res.sort(key=lambda x: (len(x), x))
for a in res:
    print(a)