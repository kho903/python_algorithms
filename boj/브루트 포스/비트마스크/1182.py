n, m = map(int, input().split())
a = list(map(int, input().split()))
res = 0
for i in range(1, (1 << n)):
    s = sum(a[k] for k in range(n) if (i & (1 << k)) > 0)
    if m == s:
        res += 1
print(res)
