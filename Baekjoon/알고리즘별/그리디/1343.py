a = list(input().split('.'))
res = ''
d = 0
for v in a:
    if len(v) % 2 != 0:
        d = 1
        print(-1)
        break
    if v:
        if len(v) % 4 == 0:
            res += "A" * len(v)
        elif len(v) % 2 == 0:
            res += ("AAAA" * (len(v) // 4) + "BB")
    res += "."

if d == 0:
    print(res[:-1])
