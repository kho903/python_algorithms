t = int(input())
a = []
for _ in range(t):
    k = int(input())
    n = int(input())
    a.append([k, n])
res = []
for i in range(t):
    if a[i][0] == 0:
        print(a[i][1])
    else:
        res = [i for i in range(1, a[i][1] + 1)]
        for w in range(a[i][0]):
            for q in range(1, len(res)):
                res[q] = res[q] + res[q - 1]
        print(res[-1])