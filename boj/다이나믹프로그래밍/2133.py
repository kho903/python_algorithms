n = int(input())
d = [0] * (n + 1)
d[0] = 1
for i in range(2, n + 1):
    d[i] = 3 * d[i - 2]
    a = i - 4
    while a >= 0:
        d[i] += 2 * d[a]
        a -= 2
print(d[n])
