n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

d = [0] * n
bridge_w = l
res = 0
s, e = 0, 0
while True:
    res += 1
    for i in range(s, e):
        d[i] += 1
        if d[i] > w:
            bridge_w += trucks[i]
            s += 1
    if s == n:
        break
    if e < n:
        if trucks[e] <= bridge_w:
            bridge_w -= trucks[e]
            d[e] += 1
            e += 1

print(res)
