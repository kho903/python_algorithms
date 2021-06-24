a = list(map(str, input().split('-')))
b = []
for i in range(len(a)):
    s = a[i].split('+')
    if len(s) == 1:
        b.append(int(s[0]))
    if len(s) >= 2:
        q = 0
        for i in s:
            q += int(i)
        b.append(q)

res = b[0]
for i in range(1, len(b)):
    res -= b[i]
print(res)