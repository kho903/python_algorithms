n = int(input())
res = 0
for i in range(1, n + 1):
    if i < 100:
        res += 1
    else:
        a = list(map(int, str(i)))
        if a[0] - a[1] == a[1] - a[2]:
            res += 1

print(res)