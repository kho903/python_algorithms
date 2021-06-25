t = int(input())

fibo = [0, 1]
for i in range(2, 45):
    fibo.append(fibo[i - 2] + fibo[i - 1])

for _ in range(t):
    n = int(input())
    res = []
    while n:
        for i in range(45):
            if fibo[i] <= n:
                t = fibo[i]
        n = n - t
        res.append(t)
        res.sort()
    for a in res:
        print(a, end=' ')
    print()
