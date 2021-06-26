n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
res = 0
a.sort()
for i in range(len(a)):
    res = max(res, a[i] * n)
    n -= 1
print(res)