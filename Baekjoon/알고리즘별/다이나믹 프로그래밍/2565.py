n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a = sorted(a, key=lambda x: x[0])
num = [0] * n

for i in range(n):
    max_num = 0
    for j in range(0, i):
        if a[i][1] > a[j][1]:
            if max_num < num[j]:
                max_num = num[j]
    num[i] = max_num + 1

print(n - max(num))
