def prime_list(n):
    a = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if a[i]:
            for j in range(i + i, n, i):
                a[j] = False
    return [i for i in range(2, n) if a[i] == True]


n = int(input())
p = prime_list(n + 1)

for i in p:
    d = []
    a = list(str(i))
    while True:
        q = 0
        for j in range(len(a)):
            q += (int(a[j]) ** 2)
        if q == 1:
            print(i)
            break
        if q not in d:
            d.append(q)
            a = list(str(q))
        else:
            break
