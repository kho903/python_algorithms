n, m = map(int, input().split())
mod = 1000000007
d = [0] * (n + 1)
d[0] = 1
for i in range(1, n + 1):
    d[i] = d[i - 1]
    if i - m >= 0:
        d[i] = (d[i] + d[i - m]) % mod

print(d[n])
