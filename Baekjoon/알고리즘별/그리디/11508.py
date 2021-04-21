n = int(input())
res = []
for _ in range(n):
    res.append(int(input()))

res.sort(reverse=True)
sum_r = 0
for i in range(len(res)):
    if i % 3 != 2:
        sum_r += res[i]

print(sum_r)
