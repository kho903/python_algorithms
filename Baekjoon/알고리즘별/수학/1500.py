s, k = map(int, input().split())
q, r = s // k, s % k

res = 1
for _ in range(k):
    if r > 0:
        res *= (q + 1)
        r -= 1
    else:
        res *= q

print(res)
