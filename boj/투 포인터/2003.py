n, m = map(int, input().split())
a = list(map(int, input().split()))
s, e = 0, 0
cnt = 0
while True:
    if s == e:
        if a[s] == m:
            cnt += 1
        if a[s] >= m:
            s += 1
            e += 1
        else:
            e += 1
    else:
        if sum(a[s:e + 1]) == m:
            cnt += 1
        if sum(a[s:e + 1]) > m:
            s += 1
        else:
            e += 1
    if e >= len(a):
        break

print(cnt)
