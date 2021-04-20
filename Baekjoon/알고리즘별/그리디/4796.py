i = 1
while True:
    l, p, v = map(int, input().split())
    res = 0
    if l == 0 and p == 0 and v == 0:
        break
    res += l * (v // p)
    res += min(v % p, l)
    print('Case %d: %d' % (i, res))
    i += 1
