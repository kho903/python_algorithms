n = int(input())
peo = []
for i in range(n):
    a = list(map(int, input().split()))
    peo.append(a)

res = [1] * n
for i in range(n - 1):
    for j in range(i, n):
        if peo[i][0] > peo[j][0] and peo[i][1] > peo[j][1]:
            res[j] += 1
        elif peo[i][0] < peo[j][0] and peo[i][1] < peo[j][1]:
            res[i] += 1

for i in res:
    print(i, end=" ")
